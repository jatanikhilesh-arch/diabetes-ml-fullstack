import streamlit as st
import requests

st.title("🩺 Diabetes Prediction App")

st.write("Enter patient details below:")

pregnancies = st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose", min_value=0)
blood_pressure = st.number_input("Blood Pressure", min_value=0)
skin_thickness = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin", min_value=0)
bmi = st.number_input("BMI", min_value=0.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=0)

if st.button("Predict"):

    url = "url = "url = "https://your-backend-name.onrender.com/predict"
"
"

    data = {
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": blood_pressure,
        "SkinThickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": dpf,
        "Age": age
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        result = response.json()
        prediction = result["prediction"]
        probability = result["probability"]

        if prediction == 1:
            st.error(f"⚠ High Risk of Diabetes\nProbability: {probability:.2f}")
        else:
            st.success(f"✅ Low Risk of Diabetes\nProbability: {probability:.2f}")
    else:
        st.error("Error connecting to API")
