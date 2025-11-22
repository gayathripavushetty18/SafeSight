import os
import csv
import json
import numpy as np

# Paths (based on your folder structure)
IMAGE_FOLDER = "../Children-Dataset"
METADATA_CSV = "../metadata.csv"
EMBEDDINGS_NPY = "./embeddings.npy"
OUTPUT_JSON = "../final_database.json"

def load_metadata():
    metadata = {}
    with open(METADATA_CSV, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            metadata[row["image_name"]] = row  # Store whole row
    return metadata

def load_embeddings():
    return np.load(EMBEDDINGS_NPY, allow_pickle=True)

def create_database():
    metadata = load_metadata()
    embeddings = load_embeddings()

    database = []

    # Ensure metadata and embeddings are aligned
    image_names = list(metadata.keys())

    if len(image_names) != len(embeddings):
        print("WARNING: Metadata count ≠ embeddings count")

    for idx, image_name in enumerate(image_names):
        record = {
            "image_name": image_name,
            "embedding": embeddings[idx].tolist(),
            "metadata": metadata[image_name]
        }
        database.append(record)

    with open(OUTPUT_JSON, "w") as f:
        json.dump(database, f, indent=4)

    print("FINAL DATABASE CREATED →", OUTPUT_JSON)
    print("Total records:", len(database))

if __name__ == "__main__":
    create_database()
