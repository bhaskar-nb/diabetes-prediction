import streamlit as st
import numpy as np
import pickle
import pandas as pd

model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("Diabetes Prediction System")
st.write("This app predicts whether a person is diabetic based on medical parameters.")

preg = st.number_input("Pregnancies", 0, 20, value=1)
glucose = st.number_input("Glucose", 0, 200, value=120)
bp = st.number_input("Blood Pressure", 0, 150, value=70)
skin = st.number_input("Skin Thickness", 0, 100, value=20)
insulin = st.number_input("Insulin", 0, 900, value=80)
bmi = st.number_input("BMI", 0.0, 60.0, value=25.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, value=0.5)
age = st.number_input("Age", 1, 120, value=30)

if st.button("Predict"):
    input_data = [preg, glucose, bp, skin, insulin, bmi, dpf, age]

    input_df = pd.DataFrame([input_data], columns=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age'])

    input_scaled = scaler.transform(input_df)
    result = model.predict(input_scaled)

    if result[0] ==1 :
        st.error("Diabetic")
    else:
        st.success("Not Diabetic")