import csv
from icalendar import Calendar
import sys

with open(sys.argv[1], "rb") as f:
    cal = Calendar.from_ical(f.read())

writer = csv.writer(sys.stdout)
writer.writerow(["datetime", "name", "email"])

for event in cal.walk("VEVENT"):
    dt = event.get("DTSTART").dt

    attendees = event.get("ATTENDEE", [])
    if not isinstance(attendees, list):
        attendees = [attendees]

    for attendee in attendees:
        email = str(attendee).replace("mailto:", "")
        name = attendee.params.get("CN", "")
        writer.writerow([dt, name, email])
