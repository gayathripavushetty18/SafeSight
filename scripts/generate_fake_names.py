from faker import Faker
import csv
import os

def generate_fake_names(image_folder, output_csv="metadata.csv"):
    fake = Faker()
    images = os.listdir(image_folder)

    with open(output_csv, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["image_name", "child_name"])

        for img in images:
            name = fake.first_name() + " " + fake.last_name()
            writer.writerow([img, name])

    print("Fake names generated and saved to metadata.csv")

if __name__ == "__main__":
    generate_fake_names("../Children-Dataset")
