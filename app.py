# app.py

import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load(r'C:/Users/mridu/OneDrive/Desktop/coding/projects/xgb_model.pkl')

st.title("💳 Credit Card Fraud Detector")

st.sidebar.header("Input Features")

inputs = {}
for i in range(1, 29):
    inputs[f"V{i}"] = st.sidebar.number_input(f"V{i}", value=0.0)
inputs["Amount"] = st.sidebar.number_input("Amount", value=0.0)
inputs["Time"] = st.sidebar.number_input("Time", value=0.0)

input_df = pd.DataFrame([inputs])

prediction = model.predict(input_df)[0]

st.subheader("Prediction:")
if prediction == 1:
    st.error("⚠️ Fraudulent Transaction Detected")
else:
    st.success("✅ Legitimate Transaction")
