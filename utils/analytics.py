"""
Analytics utility for engagement data and CSV export.
"""
import csv

def save_content_to_csv(content_list, csv_path):
    """Save a list of content dicts to a CSV file."""
    if not content_list:
        return
    keys = content_list[0].keys()
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(content_list)

def load_content_from_csv(csv_path):
    """Load content data from a CSV file."""
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader) 