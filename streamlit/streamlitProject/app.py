import streamlit as st
import numpy as np
import joblib

# Load your model
model = joblib.load('model.pkl')

# Streamlit App
st.title("Mortality Prediction App")
st.write("Enter patient details below to predict the likelihood of mortality:")

# Input fields for features
urineoutput = st.number_input("Urine Output (mL):", min_value=0.0, step=0.1)
lactate_min = st.number_input("Lactate Min:", min_value=0.0, step=0.1)
bun_mean = st.number_input("BUN Mean:", min_value=0.0, step=0.1)
sysbp_min = st.number_input("SysBP Min:", min_value=0.0, step=0.1)
metastatic_cancer = st.selectbox("Metastatic Cancer (0 = No, 1 = Yes):", [0, 1])
inr_max = st.number_input("INR Max:", min_value=0.0, step=0.1)
age = st.number_input("Age:", min_value=0, step=1)
sodium_max = st.number_input("Sodium Max:", min_value=0.0, step=0.1)
aniongap_max = st.number_input("Anion Gap Max:", min_value=0.0, step=0.1)
creatinine_min = st.number_input("Creatinine Min:", min_value=0.0, step=0.1)
spo2_mean = st.number_input("SpO2 Mean:", min_value=0.0, step=0.1)

# Prediction button
if st.button("Predict"):
    try:
        # Prepare the input data
        input_data = np.array([urineoutput, lactate_min, bun_mean, sysbp_min, metastatic_cancer,
                               inr_max, age, sodium_max, aniongap_max, creatinine_min, spo2_mean]).reshape(1, -1)
        prediction = model.predict(input_data)[0]  # Binary outcome (0 or 1)
        probability = model.predict_proba(input_data)[0][1]  # Probability of mortality (class 1)

        # Display results
        st.write(f"### Mortality Prediction: {'High Risk' if prediction == 1 else 'Low Risk'}")
        st.write(f"### Probability of Mortality: {probability:.5f}")  # Display full probability with 5 decimal places
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
