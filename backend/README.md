# Cassava-Disease-Detection
Bangkit capstone project

# Description
We use 3 GCP services to implement machine learning deployment, namely cloud function and google cloud storage, and firestore. Cloud function handle the HTTP request call from android app, cloud storage stores the ML model, and firestore for database user.

# Requirements
1. tensorflow
2. google-cloud-storage
3. Pillow

# Setup
1. Create Project in GCP (Google Cloud Platform)
2. Create Bucket for storage media in Google Cloud Storage
3. Upload model to Bucket
4. Create new function in google cloud function
5. Set entry point to predict and then copy the code in main.py to main.py in cloud
6. Change "Bucket Name", "folder in bucket/model file", "destination model file" (adjust the settings in the gcp you made)
7. Copy the reuirements.txt
8. Deploy
