# 🍅 Tomato Leaf Disease Detection Web App

A deep learning–powered web application to classify tomato leaf diseases and suggest treatments. Upload an image of a tomato leaf, and the system will detect the disease using a trained CNN model (MobileNetV2) and display the corresponding cure.

---

## 🚀 Features

- Upload and preview leaf images via a drag-and-drop interface
- Real-time disease classification using FastAPI + TensorFlow
- Suggests treatment for each detected disease
- Prediction history with timestamps
- Export prediction logs as CSV
- Mobile and desktop responsive design

---

## 🧠 Model Details

- **Architecture:** MobileNetV2 (transfer learning)
- **Framework:** TensorFlow / Keras
- **Input Size:** 224x224 RGB
- **Dataset:** [PlantVillage Tomato Dataset](https://www.kaggle.com/datasets/emmarex/plantdisease)
- **Classes:** 10 tomato leaf disease types

---

## 🛠️ Installation

### 1. Clone this repository

```bash
git clone https://github.com/your-username/tomato-leaf-disease-app.git
cd tomato-leaf-disease-app
