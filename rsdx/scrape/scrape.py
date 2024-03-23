"""Scrape experiment counts from staff pages."""

import argparse

from bs4 import BeautifulSoup
import requests


def main():
    """Main driver."""
    args = parse_args()
    homepage = get_page(args.homepage)
    result = []
    for link in homepage.find_all("a"):
        result.append(get_info(args, link["href"]))
    print(result)


def get_info(args, relative):
    """Get info from staff page."""
    page = get_page(f"{args.homepage}/{relative}")
    result = {"name": page.find("h1").string}
    for row in page.find_all("tr"):
        kind = row.find("th").string.lower()
        count = int(row.find("td").string)
        result[kind] = count
    return result


def get_page(url):
    """Get HTML page as soup."""
    response = requests.get(url)
    return BeautifulSoup(response.text, "html.parser")


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--homepage", type=str, required=True, help="Home page URL")
    return parser.parse_args()


if __name__ == "__main__":
    main()
