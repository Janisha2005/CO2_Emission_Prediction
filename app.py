import streamlit as st
import numpy as np
import joblib
pipe = joblib.load("co2_pipeline.pkl")

st.set_page_config(page_title="CO2 Emission Predictor", layout="wide")
st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://marvel-b1-cdn.bc0a.com/f00000000269980/s18391.pcdn.co/wp-content/uploads/2023/04/Co2-emissions-EVs-sustainability-1400-1000x500.jpg");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
st.title("CO2 Emission Predictor")
st.write("Predict Vehicle CO2 Emissions based on Engine Size, Cylinders, and Fuel Consumption using Polynomial Regression.")
engine_size = st.number_input("Engine Size (Liters)", 0.5, 8.0, 2.0)
cylinders = st.number_input("Cylinders", 2, 16, 4)
fuel_consumption = st.number_input("Fuel Consumption (L/100 km)", 1.0, 30.0, 8.0)

if st.button("Predict CO2 Emission"):
    input_data = np.array([[engine_size, cylinders, fuel_consumption]])
    prediction = pipe.predict(input_data)
    st.success(f"Predicted CO2 Emission: {prediction[0]:.2f} g/km")
