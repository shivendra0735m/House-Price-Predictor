import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("House_Price_Model.pkl")

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 House Price Prediction")

st.write("Enter the house details.")

area = st.number_input("Area (sq.ft)", min_value=0)

bathrooms = st.number_input(
    "Bathrooms",
    min_value=1,
    step=1
)

stories = st.number_input(
    "Stories",
    min_value=1,
    step=1
)

if st.button("Predict Price"):

    data = pd.DataFrame({
        "area":[area],
        "bathrooms":[bathrooms],
        "stories":[stories]
    })

    prediction = model.predict(data)

    st.success(f"Predicted Price: ₹ {prediction[0]:,.0f}")