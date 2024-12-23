import streamlit as st
import numpy as np
import joblib

# Load your model
model = joblib.load('model.pkl')

# Sidebar Navigation
st.sidebar.title("ML Model Web App")
st.sidebar.markdown(
    """
    <style>
    .sidebar-link {
        font-size: 16px;
        color: #000;
        text-decoration: none;
        padding: 8px 16px;
        display: block;
        border-radius: 5px;
    }
    .sidebar-link:hover {
        background-color: #f0f0f0;
        color: #ff4b4b;
    }
    .sidebar-link.active {
        background-color: #ff4b4b;
        color: white !important;
    }
    </style>
    <div>
        <a href="?page=SepsisMortalityPrediction" class="sidebar-link">Sepsis Mortality Prediction</a>
        <a href="?page=Sepsis Prediction" class="sidebar-link">Sepsis Prediction</a>
        <a href="?page=Predicting 30-Day ICU Readmissions" class="sidebar-link">Predicting 30-Day ICU Readmissions</a>
        <a href="?page=Adverse Drug Reaction (ADR) Detection" class="sidebar-link">Adverse Drug Reaction (ADR) Detection</a>
        <a href="?page=Disease Diagnosis" class="sidebar-link">Disease Diagnosis</a>
        <a href="?page=Prediction of ICU Length of Stay" class="sidebar-link">Prediction of ICU Length of Stay</a>
        <a href="?page=SAPS-II" class="sidebar-link">SAPS-II</a>
        <a href="?page=APACHE-II" class="sidebar-link">APACHE-II</a>
        <a href="?page=SOFA Score" class="sidebar-link">SOFA Score</a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Get selected page from query parameters (STABLE API)
query_params = st.query_params
page = query_params.get("page", ["SepsisMortalityPrediction"])[0]

# Routing logic based on the selected page
if page == "SepsisMortalityPrediction":
    st.title("Sepsis Mortality Prediction")
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

elif page == "DemographicData":
    st.title("Demographic Data in MIMIC")
    st.write("This is the demographic data analysis page for MIMIC.")

elif page == "MergeSepsisAge":
    st.title("Merge Sepsis with Age")
    st.write("This section is about merging sepsis data with age.")

elif page == "FindDuplicates":
    st.title("Find Duplicate Subject IDs")
    st.write("This section helps identify duplicate subject IDs in your data.")

elif page == "MIMICqSOFA":
    st.title("MIMIC qSOFA SOFA Scores")
    st.write("This section is about analyzing MIMIC qSOFA SOFA Scores.")
