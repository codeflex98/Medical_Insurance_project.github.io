import streamlit as st
import joblib
import numpy as np
import os
import pandas as pd

model_path = os.path.join(os.path.dirname(__file__), 'health_insurance_model')
model = joblib.load(model_path)

def main():
    st.title("Health Insurance Cost Prediction")

    age = st.slider("Enter your age", 18, 100)
    sex = st.selectbox('Sex', ('Male', 'Female'))
    sex_encoded = 1 if sex == 'Male' else 0
    bmi = st.number_input("Enter your BMI (Body Mass Index) value")
    children = st.slider("Enter number of children", 0, 5)
    smoker = st.selectbox("Are you a smoker?", ("Yes", "No"))
    smoker_encoded = 1 if smoker == "Yes" else 0
    region = st.selectbox("Enter your region", ("Southwest", "Southeast", "Northwest", "Northeast"))
    region_mapping = {"Southwest": 0, "Southeast": 1, "Northwest": 2, "Northeast": 3}
    region_encoded = region_mapping[region]

    # Creating a DataFrame for input data
    input_data = pd.DataFrame({'age': [age], 'sex': [sex_encoded],'bmi': [bmi],'children': [children],'smoker': [smoker_encoded],'region': [region_encoded] })

    input_data = input_data.astype(float)
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
