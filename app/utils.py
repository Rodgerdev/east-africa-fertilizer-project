import joblib
import pandas as pd
from neuralforecast.core import NeuralForecast

# Load regression model and scaler
def load_regression_model():
    model = joblib.load("models/random_forest_model.pkl")
    scaler = joblib.load("models/scaler.pkl")
    return model, scaler

# Load time series model
def load_nbeats_model():
    return NeuralForecast.load("models/nbeats_kenya")

# Load the Kenya fertilizer series
def load_fertilizer_series():
    df = pd.read_csv("models/kenya_series.csv")
    df["ds"] = pd.to_datetime(df["ds"])
    return df
