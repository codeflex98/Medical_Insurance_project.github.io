# Health Insurance Cost Prediction

## Overview
This application predicts health insurance costs based on user input such as age, BMI, number of children, smoking status, and region. The model is built using machine learning and is deployed using Streamlit.

## Features
- User-friendly web interface using **Streamlit**.
- Predicts health insurance cost based on user inputs.
- Uses a pre-trained machine learning model for prediction.

## Installation
### Prerequisites
Ensure you have **Python 3.x** installed on your system along with the following dependencies:

```
pip install streamlit joblib numpy pandas
```

## How to Run the Application
1. Clone the repository or copy the necessary files.
2. Ensure the trained model file (`health_insurance_model`) is in the same directory.
3. Open a terminal and navigate to the directory where `Health_insurance_app.py` is located.
4. Run the following command:

```
streamlit run Health_insurance_app.py
```

5. Open the provided local URL in your web browser.

## User Inputs
- **Age**: Select an age between 18 and 100.
- **Sex**: Choose between Male and Female.
- **BMI**: Enter the Body Mass Index (BMI) value.
- **Number of Children**: Select the number of children (0-5).
- **Smoker**: Choose whether the user is a smoker (Yes/No).
- **Region**: Select from Southwest, Southeast, Northwest, or Northeast.

## Model
The prediction model is trained using a dataset containing health insurance records and leverages machine learning techniques to estimate insurance costs based on input parameters.

## Expected Output
Once the user provides the required details and clicks **Predict**, the model calculates the estimated insurance cost and displays it.

## Error Handling
If any error occurs during prediction, an appropriate error message is displayed to the user.

## License
This project is open-source and available under the MIT License.

## Acknowledgments
- **Streamlit** for providing an easy-to-use UI framework.
- **Joblib** for efficient model storage and loading.
- **NumPy & Pandas** for data processing.
