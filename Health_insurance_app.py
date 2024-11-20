import streamlit as st
import joblib
import numpy as np
import os
import pandas as pd

model_path = os.path.join(os.path.dirname(__file__), 'health_insurance_model')
model = joblib.load(model_path)

import streamlit as st
import joblib  # Ensure you have joblib for loading models
import numpy as np

def main():
    # Title of the Streamlit app
    st.title("Health Insurance Cost Prediction")

    # User Inputs
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    sex = st.selectbox("Sex", ["male", "female"])
    bmi = st.number_input("BMI (Body Mass Index)", min_value=0.0, max_value=70.0, step=0.1)
    children = st.number_input("Number of Children", min_value=0, max_value=10, step=1)
    smoker = st.selectbox("Smoker Status", ["yes", "no"])
    region = st.selectbox("Region", ["northwest", "northeast", "southwest", "southeast"])

    # Preprocessing inputs for prediction
    sex_binary = 1 if sex == "male" else 0
    smoker_binary = 1 if smoker == "yes" else 0
    region_encoded = {"northwest": 0, "northeast": 1, "southwest": 2, "southeast": 3}
    region_value = region_encoded[region]

    input_features = np.array([[age, sex_binary, bmi, children, smoker_binary, region_value]])

    if st.button("Predict Insurance Cost"):
        prediction = model.predict(input_features)
        st.success(f"Predicted Health Insurance Cost: ${round(prediction[0], 2)}")
    except Exception as e:
        st.error(f"Error loading the model: {e}")

if __name__ == "__main__":
    main()

