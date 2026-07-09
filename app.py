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

# Input fields with reasonable limits
area = st.number_input(
    "Area (sq.ft)",
    min_value=500,
    max_value=20000,
    value=1500,
    step=100
)

bathrooms = st.number_input(
    "Bathrooms",
    min_value=1,
    max_value=10,
    value=2,
    step=1
)

stories = st.number_input(
    "Stories",
    min_value=1,
    max_value=5,
    value=2,
    step=1
)

if st.button("Predict Price"):

    # Extra validation
    if area < 500 or area > 20000:
        st.error("❌ Area must be between 500 and 20,000 sq.ft.")

    elif bathrooms < 1 or bathrooms > 10:
        st.error("❌ Bathrooms must be between 1 and 10.")

    elif stories < 1 or stories > 5:
        st.error("❌ Stories must be between 1 and 5.")

    else:
        data = pd.DataFrame({
            "area": [area],
            "bathrooms": [bathrooms],
            "stories": [stories]
        })

        prediction = model.predict(data)

        st.success(f"🏠 Estimated House Price: ₹ {prediction[0]:,.0f}")