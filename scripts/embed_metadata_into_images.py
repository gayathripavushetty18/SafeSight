from PIL import Image
import piexif
import csv
import os

def attach_metadata(image_folder, metadata_csv="metadata.csv"):
    with open(metadata_csv, "r") as file:
        reader = csv.DictReader(file)
        metadata = {row["image_name"]: row for row in reader}

    for img_name, data in metadata.items():
        path = os.path.join(image_folder, img_name)
        if not os.path.exists(path):
            continue

        try:
            img = Image.open(path)

            exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None}

            exif_dict["0th"][piexif.ImageIFD.ImageDescription] = str(data)

            exif_bytes = piexif.dump(exif_dict)
            img.save(path, exif=exif_bytes)

        except Exception as e:
            print("Error:", e)

    print("Metadata embedded into images.")

if __name__ == "__main__":
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Assuming the project root is one level up
    project_root = os.path.dirname(script_dir)
    
    images_path = os.path.join(project_root, "Children-Dataset")
    metadata_path = os.path.join(project_root, "metadata.csv")
    
    print(f"Processing images in: {images_path}")
    print(f"Using metadata from: {metadata_path}")
    
    if os.path.exists(images_path) and os.path.exists(metadata_path):
        attach_metadata(images_path, metadata_path)
    else:
        print("Error: Could not find 'Children-Dataset' or 'metadata.csv' in the project root.")
