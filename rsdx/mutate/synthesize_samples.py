"""Generate samples snails with genomes and locations."""


import argparse
import json
from pathlib import Path
import pandas as pd
import random

from geopy.distance import lonlat, distance


CIRCLE = 360.0
LON_LAT_PRECISION = 5
READING_PRECISION = 1
MIN_SNAIL_SIZE = 0.5
MAX_SNAIL_SIZE = 5.0
SNAIL_PRECISION = 1


def main():
    """Main driver."""
    args = parse_args()
    random.seed(args.seed)
    genomes = json.loads(Path(args.genomes).read_text())
    geo_params = get_geo_params(args)
    samples = generate_samples(args, genomes, geo_params)
    save(args, samples)


def generate_samples(args, genomes, geo_params):
    """Generate snail samples."""
    samples = []
    for sequence in genomes["individuals"]:
        point, distance = random_geo_point(**geo_params)
        if sequence[genomes["susceptible_loc"]] == genomes["susceptible_base"]:
            limit = args.mutant
        else:
            limit = args.normal
        scale = limit * distance / geo_params["radius"]
        reading = random.uniform(
            MIN_SNAIL_SIZE, MIN_SNAIL_SIZE + MAX_SNAIL_SIZE * scale
        )
        samples.append((point.longitude, point.latitude, sequence, reading))

    df = pd.DataFrame(samples, columns=("lon", "lat", "sequence", "reading"))
    df["lon"] = df["lon"].round(LON_LAT_PRECISION)
    df["lat"] = df["lat"].round(LON_LAT_PRECISION)
    df["reading"] = df["reading"].round(SNAIL_PRECISION)

    return df


def get_geo_params(args):
    """Get geographic parameters."""
    sites = pd.read_csv(Path(args.paramsdir, "sites.csv"))
    surveys = pd.read_csv(Path(args.paramsdir, "surveys.csv"))
    combined = sites.merge(surveys, how="inner", on="site")
    filtered = combined[combined["site"] == args.site].iloc[0]
    return {
        "lon": filtered["lon"],
        "lat": filtered["lat"],
        "radius": filtered["radius"],
    }


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--genomes", type=str, required=True, help="genome file")
    parser.add_argument(
        "--mutant", type=float, help="scaling factor for mutant genomes"
    )
    parser.add_argument(
        "--normal", type=float, help="scaling factor for normal genomes"
    )
    parser.add_argument("--outfile", type=str, help="output file")
    parser.add_argument(
        "--paramsdir", type=str, required=True, help="parameters directory"
    )
    parser.add_argument("--site", type=str, required=True, help="site identifier")
    parser.add_argument("--seed", type=int, required=True, help="RNG seed")
    return parser.parse_args()


def random_geo_point(lon, lat, radius):
    """Generate random geo point within radius of center."""
    center = lonlat(lon, lat)
    bearing = random.random() * CIRCLE
    dist = random.random() * radius
    return distance(kilometers=dist).destination((center), bearing=bearing), dist


def save(args, samples):
    """Save or show results."""
    if args.outfile:
        Path(args.outfile).write_text(samples.to_csv(index=False))
    else:
        print(samples.to_csv(index=False))


if __name__ == "__main__":
    main()
