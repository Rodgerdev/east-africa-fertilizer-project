import sys
print("PYTHON PATH:", sys.executable)

from fastapi import FastAPI
from app.schemas import CropInput
import joblib
import numpy as np

from app.utils import load_nbeats_model, load_fertilizer_series

# Load regression model and scaler
model = joblib.load("models/random_forest_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# Load time series model and data
nbeats_model = load_nbeats_model()
fertilizer_df = load_fertilizer_series()

app = FastAPI(title="Crop Production Predictor API")

@app.get("/")
def home():
    return {"message": "Crop Production Index Predictor is running"}

@app.post("/predict")
def predict_crop_index(data: CropInput):
    input_data = np.array([[data.fertilizer, data.cereal_yield, data.arable_land]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    return {
        "predicted_crop_production_index": float(prediction[0])
    }

@app.get("/forecast")
def forecast_fertilizer_to_2035(h=13):
    forecast_df = nbeats_model.predict()
    forecast_df = forecast_df[forecast_df['unique_id'] == 'Kenya']
    forecast_df["ds"] = forecast_df["ds"].dt.year

    return {
        "years": forecast_df["ds"].tolist(),
        "forecasted_fertilizer_consumption": forecast_df["NBEATS"].round(2).tolist()
    }
