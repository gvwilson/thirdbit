import sys
import json
import csv

raw = json.load(sys.stdin)
results = []
for (key, value) in raw.items():
    name = value['name']
    description = value['description']
    sponsor = value['sponsor']['name']
    author = value['author']['name']
    results.append((sponsor, author, name, description))
results.sort()

writer = csv.writer(sys.stdout)
writer.writerow(('sponsor', 'author', 'name', 'description'))
for r in results:
    writer.writerow(r)
