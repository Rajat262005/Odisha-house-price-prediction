import streamlit as st
import pickle
import pandas as pd

# Load trained model
model = pickle.load(open("house_price_model.pkl", "rb"))

st.set_page_config(page_title="House Price Predictor", layout="centered")

st.title("🏡 House Price Prediction App")
st.write("Enter house details to predict the estimated selling price.")

# User inputs
location = st.text_input("📍 Location (e.g., Bhubaneswar, Puri, Cuttack)")
size = st.number_input("📏 House Size (sqft)", min_value=100, max_value=10000, step=50)
rooms = st.number_input("🛏 Number of Rooms", min_value=1, max_value=20, step=1)
age = st.number_input("🏗 Age of Property (years)", min_value=0, max_value=100, step=1)
bathrooms = st.number_input("🚿 Number of Bathrooms", min_value=1, max_value=10, step=1)

if st.button("🔮 Predict Price"):
    # Create input dataframe
    input_data = pd.DataFrame([[location, size, rooms, age, bathrooms]],
                              columns=["location", "size", "rooms", "age", "bathrooms"])

    # Prediction
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Price: ₹{prediction:,.2f}")
