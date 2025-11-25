dataset zip-file link: https://drive.google.com/file/d/1FsDxgArGdR5okWN7uTKbsOZLiSVsc2NV/view?usp=sharing

SafeSight:

SafeSight is a pipeline that transforms a raw image dataset into a structured JSON database. Each image is stored as a JSON object containing its file path, metadata, and embeddings. This makes the database suitable for fast retrieval, AI workflows, and machine learning tasks. Large datasets are managed locally to avoid GitHub size limitations, while the final database remains lightweight and easy to use.

Project overview:

This project converts an image dataset into a final JSON database. The workflow includes metadata generation, embeddings creation, and merging everything into a single structured JSON file. The goal is to create a clean dataset representation that can be used directly in other tools, models, or applications.

Workflow:

1. Dataset preparation
   Collected a dataset of images stored locally. Large dataset files were intentionally excluded from GitHub to avoid size limit issues.

2. Metadata generation
   Created fake metadata for each image. Metadata includes details such as ID, labels, descriptions, and other structured information.

3. Embeddings creation
   Generated embeddings (numerical feature vectors) for every image. These embeddings can be used for similarity search or machine learning tasks.

4. Final database construction
   Combined the image paths, metadata, and embeddings into a single JSON file named final_database.json.
   Each image has its own JSON object containing:

   * image_path
   * metadata
   * embedding

5. Large file management
   Large files like Children-Dataset.zip and Children-Dataset/ were removed from git history and added to .gitignore.
   The git history was cleaned using git filter-repo to prevent GitHub push errors.

Repository structure:

```
SafeSight/
├─ final_database.json
├─ scripts/
├─ .gitignore
└─ README.md
```

Highlights:

* Each image is represented as a structured JSON object.
* Metadata and embeddings allow efficient machine learning usage.
* The final JSON database replaces the need to store large datasets in the repo.
* Clean git history ensures smooth GitHub pushes.

Usage:

You can load and use the final JSON database in any programming language. Example in Python:
import json

with open("final_database.json", "r") as f:
    data = json.load(f)

print(data[0]['image_path'])
print(data[0]['metadata'])
print(data[0]['embedding'])
```

