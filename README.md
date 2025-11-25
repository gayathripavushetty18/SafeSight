dataset zip-file link: https://drive.google.com/file/d/1FsDxgArGdR5okWN7uTKbsOZLiSVsc2NV/view?usp=sharing

SAFESIGHT

Project overview:

SafeSight is an AI-driven system designed to assist in identifying missing children using facial recognition and a structured database. The goal is to build an automated pipeline that detects missing children from live CCTV feeds, public images, or manual uploads and alerts the appropriate authorities.

Since real missing-child datasets are sensitive and hard to access, the project begins by constructing a synthetic but realistic database. This includes collecting images, generating metadata (such as names, age, gender, labels), producing facial embeddings, and storing everything in a clean JSON database. This database acts as the “ground truth” reference for the AI model.

The long-term goal is to deploy an end-to-end detection system that compares incoming faces against this database in real-time and sends automated notifications to the nearest police station if a match is detected.

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

   To be continued>>>>>

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
```
import json

with open("final_database.json", "r") as f:
    data = json.load(f)

print(data[0]['image_path'])
print(data[0]['metadata'])
print(data[0]['embedding'])
```

# Logical Next Steps (Fine-Tuned Roadmap)

Below is the refined and structured plan for what you should do next.

---

## Step 1 — Prepare the Data for Training

Now that you have:

• images
• metadata
• embeddings
• final JSON representation

You need to prepare this for model training.

What to do:

1. Split the dataset into:
   • Train set (80%)
   • Test set (20%)

2. Ensure each image has:
   • Image path
   • Normalized metadata (age group, gender, tags)
   • Embeddings (you already have them, good)

3. Define labels
   In missing-child detection, the label is usually the child’s unique ID or name.

This prepares the dataset for supervised model learning.

---

## Step 2 — Choose the Model Architecture

Since your goal is face matching, you don’t need to train from scratch.

Use a face-recognition model architecture like:

• FaceNet
• ArcFace
• ResNet-based face encoders
• MobileFaceNet

You already created embeddings — so your model step becomes simpler:

You don’t train a full CNN.
Instead, you train or fine-tune a **classifier** or **similarity matcher** over the embeddings.

That means your model is basically:

feature_vector → classifier → child identity

Or use:

embedding_distance(image, database) → match OR no match

This is more efficient and realistic.

---

## Step 3 — Build the Matching Engine

This is the core of your detection system.

How it works:

1. Take an image from CCTV / uploaded photo
2. Extract its embedding using the same encoder
3. Compare it to every embedding in final_database.json
4. Use cosine similarity or Euclidean distance
5. If distance < threshold → This is a match
6. Return identity + metadata + match confidence

This completes the “AI detection” loop.

---

## Step 4 — Add Location Metadata (Critical)

Since alerts need to go to the local police station, each record should have:

• last known location
• home district / city
• missing-from location
• case ID

Also, during real-time detection you need to extract:

• detection location (GPS or CCTV location)

Then, match this to the nearest police station.

This could be done using:

• GIS mapping
• Simple lookup table of police station areas
• Google Maps API (optional)

---

## Step 5 — Build the Alerting System

If a match is found:

1. Prepare an automated SMS format
   Example:
   “Possible match found for missing child: <Name>, <Age>. Detected at <Location>. Match accuracy: 92%.”

2. Use an SMS API such as:
   • Twilio
   • Fast2SMS
   • MSG91 (used widely in India)

3. Connect detection system → SMS API → police phone number

This creates a functional notification loop.

---

## Step 6 — Build an API/Backend

To make the system usable by apps or websites, create a backend service:

Endpoints such as:

POST /detect
POST /send-alert
GET /child/<id>
GET /matches

You can use:

• FastAPI
• Flask
• Node.js

FastAPI is strongly recommended.

---

## Step 7 — Build a Minimal UI

Optional but useful for a showcase or hackathon:

• Upload image → get detection result
• See match probability
• View database entries
• Map view for detection location
• Notification history

React + Tailwind or HTML/Bootstrap is enough.

---

## Step 8 — Real-Time Deployment (Future)

Later, you can integrate:

• CCTV feed → face detection → embedding creation → matching
• On-device model for faster inference
• Cloud deployment (AWS, Render, GCP)

---

# Complete Next-Steps Summary (Short Version)

1. Prepare dataset
2. Split into train/test
3. Use the embeddings to train a classifier or do similarity matching
4. Build a face-matching engine
5. Add location metadata
6. Build an alert system (SMS to local police)
7. Create backend APIs
8. Create a lightweight UI
9. Integrate with real-time video input (future upgrade)

---
