import streamlit as st
import requests

st.set_page_config(page_title="Diabetes Prediction", page_icon="🩺")

st.title("🩺 Diabetes Prediction App")
st.write("Enter patient details below:")

# ---- INPUTS ----
pregnancies = st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose", min_value=0)
blood_pressure = st.number_input("Blood Pressure", min_value=0)
skin_thickness = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin", min_value=0)
bmi = st.number_input("BMI", min_value=0.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=0)

# ---- BUTTON ----
if st.button("Predict"):

    url = "http://127.0.0.1:8000/predict"

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

    try:
        response = requests.post(url, json=data)

        if response.status_code == 200:
            result = response.json()

            prediction = result["prediction"]
            probability = result["probability"]
            risk_level = result.get("risk_level", "Not Available")
            explanation = result.get("explanation", "")
            risk_factors = result.get("risk_factors", "")

            st.subheader("📊 Prediction Results")

            # Risk Display
            if prediction == 1:
                st.error(f"⚠ {risk_level}")
            else:
                st.success(f"✅ {risk_level}")

            st.write(f"**Probability:** {probability:.2f}")

            # Progress bar for probability
            st.progress(float(probability))

            # Explanation
            st.subheader("🧠 Explanation")
            st.info(explanation)

            # Risk Factors (if available)
            if risk_factors:
                st.subheader("🔍 Identified Risk Factors")
                st.warning(risk_factors)

        else:
            st.error("Error connecting to API")

    except Exception as e:
        st.error(f"Connection Error: {e}")
