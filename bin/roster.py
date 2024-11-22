import argparse
import plotly.express as px
import sqlite3


QUERY = """\
select location.latitude, location.longitude, count(*)
from location join person join member
on (person.birthplace = location.ident)
and (person.ident = member.person)
and (member.role in ('CSC494', 'CSC495'))
where (person.birthplace != -1)
group by location.ident;
"""

def main():
    """Main driver."""
    opts = parse_args()
    lat, lon, num = read_data(opts)
    fig = px.scatter_mapbox(
        lat=lat,
        lon=lon,
        size=num,
        mapbox_style="open-street-map",
        zoom=1,
        width=1200
    )
    fig.show()


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", type=str, default=None, help="database file")
    return parser.parse_args()


def read_data(opts):
    """Get data from database."""
    connection = sqlite3.connect(opts.db)
    cursor = connection.execute(QUERY)
    rows = cursor.fetchall()
    lat = [r[0] for r in rows]
    lon = [r[1] for r in rows]
    num = [r[2] for r in rows]
    return lat, lon, num


if __name__ == "__main__":
    main()
