import streamlit as st
import joblib
import numpy as np
import os
import pandas as pd

model_path = os.path.join(os.path.dirname(__file__), 'health_insurance_model')
model = joblib.load(model_path)

def main():
    st.title("Health Insurance Cost Prediction")

    # Input fields
    p1 = st.slider("Enter your age", 18, 100)
    s1 = st.selectbox('Sex', 0, 1))
    p2 = 1 if s1 == 'Male' else 0
    p3 = st.number_input("Enter your BMI (Body Mass Index) value")
    p4 = st.slider("Enter number of children", 0, 5)
    s2 = st.selectbox("Are you a smoker?", 0, 1)
    p5 = 1 if s2 == "Yes" else 0
    s6 = st.selectbox("Enter your region", 0, 1, 2, 3)
    
    print(f"Inputs: {p1}, {p2}, {p3}, {p4}, {p5}, {p6}")
    input_data = np.array([[p1, p2, p3, p4, p5, p6]])
    print(f"Input data shape: {input_data.shape}")

    # Predict button
    if st.button("Predict"):
        try:
            prediction = model.predict(input_data)
            st.balloons() 
            st.success(f"Your insurance cost is {round(prediction[0], 2)} US Dollars")
        except Exception as e:
            st.error(f"Error in prediction: {e}")

if __name__ == '__main__':
    main()
