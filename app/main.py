from fastapi import FastAPI
from app.schemas import CropInput
import joblib
import numpy as np

# Load model and scaler
model = joblib.load("models/random_forest_model.pkl")
scaler = joblib.load("models/scaler.pkl")

app = FastAPI(title="Crop Production Predictor API")

@app.get("/")
def home():
    return {"message": "Crop Production Index Predictor is running"}

@app.post("/predict")
def predict_crop_index(data: CropInput):
    # Prepare input for model
    input_data = np.array([[data.fertilizer, data.cereal_yield, data.arable_land]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    return {
        "predicted_crop_production_index": float(prediction[0])
    }
