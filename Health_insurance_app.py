import streamlit as st
import joblib
import numpy as np
import os

model_path = os.path.join(os.path.dirname(__file__), 'health_insurance_model')
model = joblib.load("D:/Hochschule Fresenius notes (sem3)/Artifical Intelligence and Machine Learning/Medical_Insurance/health_insurance_model")

def main():
    st.title("Health Insurance Cost Prediction")

    # Input fields
    p1 = st.slider("Enter your age", 18, 100)
    s1 = st.selectbox('Sex', ('Male', 'Female'))
    p2 = 1 if s1 == 'Male' else 0
    p3 = st.number_input("Enter your BMI (Body Mass Index) value")
    p4 = st.slider("Enter number of children", 0, 5)
    s2 = st.selectbox("Are you a smoker?", ("Yes", "No"))
    p5 = 1 if s2 == "Yes" else 0
    s3 = st.selectbox("Enter your region", ("Southwest", "Southeast", "Northwest", "Northeast"))
    if s3 == "Southwest":
        p6 = 0
    elif s3 == "Southeast":
        p6 = 1
    elif s3 == "Northwest":
        p6 = 2
    else:
        p6 = 3

    # Input array
    input_data = np.array([[p1, p2, p3, p4, p5, p6]])

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
