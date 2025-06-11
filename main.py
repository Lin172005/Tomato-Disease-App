from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import shutil
import os
import csv
from datetime import datetime
from predict import predict_image

app = FastAPI()

# Directories
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
os.makedirs("temp", exist_ok=True)

LOG_FILE = "prediction_log.csv"

# Create log file with headers if it doesn't exist
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Filename", "Prediction", "Confidence", "Treatment"])

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request, file: UploadFile = File(...)):
    file_location = f"temp/{file.filename}"
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)

    class_name, confidence, treatment = predict_image(file_location)

    # Log prediction
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), file.filename, class_name, f"{confidence:.2f}", treatment])

    os.remove(file_location)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": f"{class_name} ({confidence * 100:.2f}%)",
        "treatment": treatment
    })
