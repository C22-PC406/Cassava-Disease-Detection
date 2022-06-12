from google.cloud import storage
import tensorflow as tf
from PIL import Image
import numpy as np

# Bucket name
BUCKET_NAME = 'Bucket Name' #change this

# Class name
class_names = [
    "Cassava Bacterial Blight (CBB)",
    "Cassava Brown Streak Disease (CBSD)",
    "Cassava Green Mottle (CGM)",
    "Cassava Mosaic Disease (CMD)",
    "Healthy"
]

model = None

# Download blob
def download_blob(bucket_name, source_blob_name, destination_file_name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

# Predict
def predict(request):
    global model
    if model is None:
        download_blob(
            BUCKET_NAME,
            "folder in bucket/model file", # change this
            "destination model file", # change this
        )
        model = tf.keras.models.load_model("destination model file") # change this

    image = request.files["file"]
    image = np.array(
        Image.open(image).convert("RGB").resize((256, 256)) # image resizing
    )
    img_batch = np.expand_dims(image, 0)
    predictions = model.predict(img_batch)

    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)

    return {
        "class": predicted_class,
        "confidence": confidence
    }