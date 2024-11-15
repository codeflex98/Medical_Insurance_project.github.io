import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), 'health_insurance_model')
model = joblib.load(model_path)

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
    s6 = st.selectbox("Enter your region", ("Southwest", "Southeast", "Northwest", "Northeast"))

    if s6 == "Southwest":
        p6 = 0
    elif s6 == "Southeast":
        p6 = 1
    elif s6 == "Northwest":
        p6 = 2
    else:  # "Northeast"
        p6 = 3

     # Ensure input values are correctly typed
    p1 = int(p1)
    p3 = float(p3)
    p4 = int(p4)
    p5 = int(p5)
    p6 = int(p6)

    # Input array converted to DataFrame
    input_data = np.array([[p1, p2, p3, p4, p5, p6]])
    columns = ["age", "sex", "bmi", "children", "smoker", "region"]
    input_df = pd.DataFrame(input_data, columns=columns)

    # Predict button
    if st.button("Predict"):
        try:
            prediction = model.predict(input_df)
            st.success(f"The predicted insurance cost is: ${prediction[0]:,.2f}")
        except Exception as e:
            st.error(f"Error in prediction: {e}")

if __name__ == '__main__':
    main()
