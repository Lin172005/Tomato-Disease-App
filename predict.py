import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load trained model
model = load_model("tomato_disease_model.h5")

# Class labels (customize based on your dataset)
class_names = ['Bacterial Spot', 'Early Blight', 'Late Blight', 'Leaf Mold', 'Septoria Leaf Spot',
               'Spider Mites', 'Target Spot', 'Yellow Leaf Curl Virus', 'Mosaic Virus', 'Healthy']

# Treatment suggestions
treatments = {
    'Bacterial Spot': "Use copper-based fungicides. Remove infected leaves.",
    'Early Blight': "Use fungicides like chlorothalonil. Rotate crops.",
    'Late Blight': "Remove infected plants. Apply fungicide quickly.",
    'Leaf Mold': "Improve air circulation. Use fungicide if needed.",
    'Septoria Leaf Spot': "Remove lower leaves. Apply fungicide.",
    'Spider Mites': "Spray water on underside of leaves. Use neem oil.",
    'Target Spot': "Maintain good spacing. Apply approved fungicides.",
    'Yellow Leaf Curl Virus': "Use insecticidal soap. Remove infected plants.",
    'Mosaic Virus': "Remove infected plants. Disinfect tools.",
    'Healthy': "No disease detected. Maintain proper care."
}

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0]
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence = prediction[index]
    treatment = treatments.get(class_name, "No treatment found.")

    return class_name, confidence, treatment
