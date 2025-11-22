from faker import Faker
import csv
import random
from datetime import datetime, timedelta

def add_fake_metadata(metadata_csv="metadata.csv"):
    fake = Faker()
    updated_rows = []

    with open(metadata_csv, "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    for row in rows:

        row["age"] = random.randint(4, 15)

        row["missing_from_city"] = fake.city()

        missing_days = random.randint(1, 365)
        missing_date = datetime.now() - timedelta(days=missing_days)
        row["missing_date"] = missing_date.strftime("%Y-%m-%d")

        row["description"] = fake.sentence()

        updated_rows.append(row)

    with open(metadata_csv, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=updated_rows[0].keys())
        writer.writeheader()
        writer.writerows(updated_rows)

    print("Metadata updated successfully.")

if __name__ == "__main__":
    add_fake_metadata()
