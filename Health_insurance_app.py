import streamlit as st
import joblib
import numpy as np
import os
model_path = os.path.join(os.path.dirname(__file__), 'health_insurance_model')
model = joblib.load(model_path)

def main():
    st.title("Health Insurance Cost Prediction")

    
    p1 = st.slider("Enter your age", 18, 100)
    s1 = st.selectbox('Sex',('Male', 'Female'))
    if s1 =='Male':
        p2 = 1
    else:
        p2 = 0
    p3 = st.number_input("Enter your BMI(Body mass index) value")
    p4 = st.slider("Enter number of children",0, 5)
    s2 = st.selectbox("Are you a smoker? ", ("Yes", "No"))
    if s2 == "Yes":
        p5 = 1
    else:
        p5 = 0
    
    #p6 = st.slider("Enter your region", 1,4)#"southwest":0, "southeast":1, "northwest":2, "northeast":3
    s3 = st.selectbox("Enter your region", ("Southwest", "Southeast", "Northwest", "Northeast")) 
    if s2 == "Southwest":
        p6 = 0
    elif s2 == "Southeast":
        p6 = 1
    elif s3 == "Northwest":
        p6 = 2
    else:
        p6 = 3
        
    # Debugging statements
    print(f"Inputs: {p1}, {p2}, {p3}, {p4}, {p5}, {p6}")
    input_data = np.array([[p1, p2, p3, p4, p5, p6]])
    print(f"Input data shape: {input_data.shape}")

    # Example result (replace with your prediction logic)
    if st.button("Predict"):
        try:
            prediction = model.predict(input_data)
            st.balloons() 
            st.success(f"Your insurance cost is {round(prediction[0], 2)} US Dollars")
        except Exception as e:
            st.error(f"Error in prediction: {e}")

if __name__ == '__main__':
    main()
