import os
import csv
import numpy as np
import cv2
from deepface import DeepFace

def generate_embeddings(image_folder, metadata_csv="../metadata.csv", output="embeddings.npy"):

    embeddings = []
    image_names = []

    with open(metadata_csv, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    for row in rows:
        img_path = os.path.join(image_folder, row["image_name"])
        if not os.path.exists(img_path):
            print("Missing:", img_path)
            continue

        try:
            # Load and downscale manually -> avoids TensorFlow freeze
            img = cv2.imread(img_path)
            if img is None:
                print("Cannot open:", img_path)
                continue

            img = cv2.resize(img, (160, 160))  # FIX: Prevent CPU freeze

            # Fast, CPU-friendly model
            emb_info = DeepFace.represent(
                img,
                model_name="SFace",      # FASTEST and accurate
                enforce_detection=False,  # skip alignment
            )

            emb = emb_info[0]["embedding"]

            embeddings.append(emb)
            image_names.append(row["image_name"])

        except Exception as e:
            print("Error processing:", img_path, "|", e)
            continue

    np.save(output, np.array(embeddings))
    print("\n✔ Saved embeddings:", output)
    print("✔ Total embeddings:", len(embeddings))


if __name__ == "__main__":
    generate_embeddings("../Children-Dataset")
