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
    age = st.slider("Enter your age", 18, 100)
    sex = st.selectbox('Sex', ('Male', 'Female'))
    
    sex_encoded = 1 if sex == 'Male' else 0
    
    bmi = st.number_input("Enter your BMI (Body Mass Index) value")
    
    children = st.slider("Enter number of children", 0, 5)
    smoker = st.selectbox("Are you a smoker?", ("Yes", "No"))
    
    smoker_encoded = 1 if smoker == "Yes" else 0
    
    region = st.selectbox("Enter your region", ("Southwest", "Southeast", "Northwest", "Northeast"))
    if region == "Southwest":
        region_encoded = 0
    elif region == "Southeast":
        region_encoded = 1
    elif region == "Northwest":
        region_encoded = 2
    else:
        region_encoded = 3

   input_data = pd.DataFrame({'age': [age],'sex': [sex_encoded],'bmi': [bmi],'children': [children],'smoker': [smoker_encoded],'region': [region_encoded] })

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
