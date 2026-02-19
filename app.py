from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np


app = FastAPI()



model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

class InputData(BaseModel):
    Pregnancies: float
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: float

@app.get("/")
def home():
    return {"message": "Diabetes Prediction API is running"}

@app.post("/predict")
def predict(data: InputData):

    features = np.array([[
        data.Pregnancies,
        data.Glucose,
        data.BloodPressure,
        data.SkinThickness,
        data.Insulin,
        data.BMI,
        data.DiabetesPedigreeFunction,
        data.Age
    ]])
    scaled = scaler.transform(features)
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    # 🔥 Rule-Based Explanation Logic

    if prediction == 1:
        if probability >= 0.80:
            risk_level = "High Risk"
            explanation = (
                "The patient shows a high probability of diabetes. "
                "Elevated glucose and other contributing factors suggest "
                "immediate medical consultation and lifestyle changes."
            )
        elif probability >= 0.60:
            risk_level = "Moderate Risk"
            explanation = (
                "The patient shows moderate risk of diabetes. "
                "Monitoring blood sugar levels and improving diet and exercise "
                "habits is recommended."
            )
        else:
            risk_level = "Low Risk (Borderline)"
            explanation = (
                "The probability indicates a low but notable risk. "
                "Preventive lifestyle adjustments are advisable."
            )
    else:
        risk_level = "No Diabetes Detected"
        explanation = (
            "The model predicts that the patient is not diabetic. "
            "Continue maintaining a healthy lifestyle and regular checkups."
        )

    return {
        "prediction": int(prediction),
        "probability": float(probability),
        "risk_level": risk_level,
        "explanation": explanation
    }

