"""Generate genomes with random mutations."""

import argparse
from dataclasses import dataclass, asdict
import json
from pathlib import Path
import random

# Bases.
DNA = "ACGT"

# Probabilities of single nucleotide variations. The original base (from the reference
# genome) will be select 50% of the time; the other three bases will be shuffled and
# one selected per person with the given probabilities.
SNP_PROBS = (0.50, 0.25, 0.13, 0.12)


@dataclass
class GenePool:
    """Keep track of generated genomes."""

    length: int
    reference: str
    individuals: list[str]
    locations: list[int]
    susceptible_loc: int = 0
    susceptible_base: str = ""


def main():
    """Main driver."""
    args = parse_args()
    random.seed(args.seed)
    genomes = random_genomes(
        args.length,
        args.num_genomes,
        args.num_snp,
        args.prob_other,
    )
    add_susceptibility(genomes)
    save(args.outfile, genomes)


def add_susceptibility(genomes):
    """Add indication of genetic susceptibility."""
    if not genomes.locations:
        return
    loc = _choose_one(genomes.locations)
    choices = {ind[loc] for ind in genomes.individuals} - {genomes.reference[loc]}
    genomes.susceptible_loc = loc
    genomes.susceptible_base = _choose_one(list(choices))


def parse_args():
    """Get command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--length", type=int, required=True, help="genome length")
    parser.add_argument("--outfile", type=str, default=None, help="output file")
    parser.add_argument(
        "--num_genomes", type=int, required=True, help="number of genomes"
    )
    parser.add_argument("--num_snp", type=int, required=True, help="number of SNPs")
    parser.add_argument(
        "--prob_other", type=float, required=True, help="probability of other mutation"
    )
    parser.add_argument("--seed", type=int, required=True, help="RNG seed")

    args = parser.parse_args()

    assert args.length > 0, f"Require --length > 0 not {args.length}"
    assert args.num_genomes > 0, f"Require --genomes > 0 not {args.num_genomes}"
    assert args.num_snp >= 0, f"Require --num_snp >= 0 not {args.num_snp}"
    assert args.prob_other >= 0.0, f"Require --prob_other >= 0.0 not {args.prob_other}"

    return args


def random_bases(length):
    """Generate a random sequence of bases of the specified length."""
    assert 0 < length
    return "".join(random.choices(DNA, k=length))


def random_genomes(length, num_genomes, num_snp, prob_other):
    """Generate a set of genomes with specified number of point mutations."""
    assert 0 <= num_snp <= length

    # Reference genomes and specific genomes to modify.
    reference = random_bases(length)
    individuals = [reference] * num_genomes

    # Locations for SNPs.
    locations = random.sample(list(range(length)), num_snp)

    # Introduce significant mutations.
    for loc in locations:
        candidates = _other_bases(reference, loc)
        bases = [reference[loc]] + random.sample(candidates, k=len(candidates))
        individuals = [_mutate_snps(reference, ind, loc, bases) for ind in individuals]

    # Introduce other random mutations.
    other_locations = list(set(range(length)) - set(locations))
    individuals = [
        _mutate_other(ind, prob_other, other_locations) for ind in individuals
    ]

    # Return structure.
    individuals.sort()
    locations.sort()
    return GenePool(
        length=length, reference=reference, individuals=individuals, locations=locations
    )


def save(outfile, genomes):
    """Save or report generated."""
    as_text = json.dumps(asdict(genomes), indent=4)
    if outfile:
        Path(outfile).write_text(as_text)
    else:
        print(as_text)


def _mutate_snps(reference, genome, loc, bases):
    """Introduce single nucleotide polymorphisms at the specified location."""
    choice = _choose_one(bases, SNP_PROBS)
    return genome[:loc] + choice + genome[loc + 1 :]


def _mutate_other(genome, prob, locations):
    """Introduce up to `max_num_mutations` at specified locations."""
    if random.random() > prob:
        return genome
    loc = random.sample(locations, k=1)[0]
    base = random.choice(_other_bases(genome, loc))
    genome = genome[:loc] + base + genome[loc + 1 :]
    return genome


def _choose_one(values, weights=None):
    """Convenience wrapper to choose a single items with weighted probabilities."""
    return random.choices(values, weights=weights, k=1)[0]


def _other_bases(seq, loc):
    """Create a list of bases minus the one in the sequence at that location.

    We return a list instead of a set because the result is used in random.choices(),
    which requires an indexable sequence. We sort for reproducibility.
    """
    return list(sorted(set(DNA) - {seq[loc]}))


if __name__ == "__main__":
    main()
