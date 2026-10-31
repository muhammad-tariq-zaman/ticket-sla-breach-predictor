"""Predict SLA breaches from a ticket CSV (id,created,sla_hours).

Usage: python3 main.py tickets.csv --now 2026-10-29T12:00:00
Bands: BREACHED, AT RISK (under 25% of SLA time left), OK.
"""
import argparse
import csv
import sys
from datetime import datetime


def band(created, sla_hours, now):
    elapsed = (now - datetime.fromisoformat(created)).total_seconds() / 3600
    remaining = sla_hours - elapsed
    if remaining < 0:
        return "BREACHED"
    if sla_hours and remaining / sla_hours < 0.25:
        return "AT RISK"
    return "OK"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="Ticket CSV file")
    parser.add_argument("--now", default=None, help="Reference time ISO (default: now)")
    args = parser.parse_args(argv)
    now = datetime.fromisoformat(args.now) if args.now else datetime.now()
    breached = 0
    with open(args.path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            state = band(row["created"], float(row["sla_hours"]), now)
            breached += state == "BREACHED"
            print(f"{row['id']}: {state}")
    print(f"{breached} ticket(s) breached.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
