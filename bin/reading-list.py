import csv
import sys

with open(sys.argv[1], newline="") as f:
    rows = list(csv.DictReader(f))

with open(sys.argv[2], "w") as f:
    f.write('---\ntitle: "Reading List"\ntemplate: page\n---\n\n')
    f.write("| Title | Author | ISBN | Year |\n")
    f.write("| ----- | ------ | ---- | ---- |\n")
    for row in rows:
        f.write(f"| {row['title']} | {row['author']} | {row['isbn']} | {row['year']} |\n")
