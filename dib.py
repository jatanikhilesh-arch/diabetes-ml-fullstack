import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score
import joblib

df= pd.read_csv("diabetes.csv")
print(df.head())

x=df.drop("Outcome", axis=1)
y= df["Outcome"]

x_train,x_test,y_train,y_test=train_test_split(x,y, test_size=0.2, random_state=42)

scaler= StandardScaler()
x_train_scaled= scaler.fit_transform(x_train)
x_test_scaled= scaler.transform(x_test)

model= RandomForestClassifier()
model.fit(x_train_scaled,y_train)

y_pred= model.predict(x_test_scaled)

print("accuracy:", accuracy_score(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, model.predict_proba(x_test_scaled)[:,1]))

joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")