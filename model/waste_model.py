import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Load trained model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'waste_model.h5')
model = load_model(MODEL_PATH)

# 9 class labels
class_labels = [
    'battery', 'biological', 'brown-glass', 'cardboard', 
    'green-glass', 'metal', 'paper', 'plastic', 'white-glass'
]

# Info for each waste class
waste_info = {
    'battery': "Hazardous waste. Dispose at battery collection centers.",
    'biological': "Biodegradable waste. Suitable for composting.",
    'brown-glass': "Recyclable. Clean and drop at glass bins.",
    'cardboard': "Dry cardboard is recyclable. Flatten before disposal.",
    'green-glass': "Recyclable. Use local bottle recycling services.",
    'metal': "Recyclable. Do not mix with food residue.",
    'paper': "Dry paper is recyclable. Avoid contaminated paper.",
    'plastic': "Most plastics are recyclable. Check local rules.",
    'white-glass': "Recyclable. Dispose at designated bins for white glass."
}

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def predict_waste(img_path):
    processed = preprocess_image(img_path)
    prediction = model.predict(processed)
    predicted_class = class_labels[np.argmax(prediction)]
    info = waste_info.get(predicted_class, "No information available.")
    return predicted_class, info
