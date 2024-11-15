import streamlit as st
import joblib
import numpy as np
import os

model_path = os.path.join(os.path.dirname(__file__), 'health_insurance_model')
model = joblib.load(model_path)

def main():
    st.title("Health Insurance Cost Prediction")

    # User input for age
    age = st.slider("Enter your age", 18, 100)
    
    # User input for sex
    sex = st.selectbox('Sex', ('Male', 'Female'))
    if sex == 'Male':
        sex_encoded = 1
    else:
        sex_encoded = 0

    # User input for BMI
    bmi = st.number_input("Enter your BMI (Body Mass Index) value", value=25.0, min_value=10.0, max_value=60.0)
    
    # User input for number of children
    children = st.slider("Enter number of children", 0, 5)
    
    # User input for smoking status
    smoker = st.selectbox("Are you a smoker?", ("Yes", "No"))
    if smoker == "Yes":
        smoker_encoded = 1
    else:
        smoker_encoded = 0
    
    # User input for region
    region = st.selectbox("Enter your region", ("Southwest", "Southeast", "Northwest", "Northeast"))
    if region == "Southwest":
        region_encoded = 0
    elif region == "Southeast":
        region_encoded = 1
    elif region == "Northwest":
        region_encoded = 2
    else:
        region_encoded = 3
    
    # Prepare input data for the model
    input_data = np.array([[age, sex_encoded, bmi, children, smoker_encoded, region_encoded]])
    
    # Predict using the loaded model
    prediction = model.predict(input_data)
    
    # Display the prediction
    st.success(f"The predicted insurance cost is: ${prediction[0]:.2f}")

if __name__ == '__main__':
    main()
