import streamlit as st
import requests
import pandas as pd

st.title("Crop Production Index Predictor")

# Input fields
fertilizer = st.number_input("Fertilizer consumption (kg/ha)")
cereal_yield = st.number_input("Cereal yield (kg/ha)")
arable_land = st.number_input("Arable land (hectares per person)")

if st.button("Predict"):
    input_data = {
        "fertilizer": fertilizer,
        "cereal_yield": cereal_yield,
        "arable_land": arable_land
    }

    response = requests.post("http://127.0.0.1:8001/predict", json=input_data)
    
    if response.status_code == 200:
        prediction = response.json()["predicted_crop_production_index"]
        st.success(f"Predicted Crop Production Index: {prediction:.2f}")
    else:
        st.error("Something went wrong. Check the API.")

st.header("Forecast Fertilizer Consumption to 2029")

if st.button("Show Forecast"):
    response = requests.get("http://127.0.0.1:8001/forecast")
    
    if response.status_code == 200:
        data = response.json()

        forecast_df = pd.DataFrame({
    "Year": data["years"],  # Use plain integers directly
    "Fertilizer Consumption": data["forecasted_fertilizer_consumption"]
})

        forecast_df.set_index("Year", inplace=True)
        
        st.line_chart(forecast_df)
        
        st.dataframe(forecast_df)

    else:
        st.error("Could not load forecast.")


