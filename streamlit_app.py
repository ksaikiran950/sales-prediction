import streamlit as st
import pickle
import numpy as np

st.title("🚗 Car Purchase Amount Predictor")
st.markdown("Enter customer information below to predict car purchase amount.")

# Input fields
age = st.slider("Age", 20, 80, 35)
gender = st.radio("Gender", ("Male", "Female"))
salary = st.number_input("Annual Salary ($)", min_value=10000, step=500, value=50000)
credit_debt = st.number_input("Credit Card Debt ($)", min_value=0.0, step=100.0, value=1000.0)
net_worth = st.number_input("Net Worth ($)", min_value=0.0, step=1000.0, value=100000.0)

if gender == "Male":
    gender_val = 1
else:
    gender_val = 0

# Load model
model = pickle.load(open("models/model.pkl", "rb"))

# Predict
if st.button("Predict"):
    input_data = np.array([[age, gender_val, salary, credit_debt, net_worth]])
    prediction = model.predict(input_data)
    st.success(f"Estimated Car Purchase Amount: ${prediction[0]:,.2f}")
