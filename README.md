# Sepsis Mortality Prediction Web Application

A machine learning-powered web application for predicting sepsis mortality risk in ICU patients using clinical data from the MIMIC-III database. This project provides both Flask and Streamlit implementations for healthcare professionals to assess patient risk levels.

## 🎯 Overview

Sepsis is a life-threatening condition that requires rapid identification and treatment. This application uses an **XGBoost machine learning model** trained on MIMIC-III clinical data to predict the mortality risk of sepsis patients based on key clinical features.

### Key Features

- 🔬 **ML-Powered Predictions**: XGBoost model trained on real ICU patient data
- 🌐 **Dual Web Interfaces**: Both Flask and Streamlit implementations
- 📊 **Real-time Risk Assessment**: Instant mortality probability calculations
- 💉 **Clinical Feature Input**: 11 key clinical parameters for accurate predictions
- 📈 **Data Analysis**: Jupyter notebooks for model development and analysis

## 🏗️ Project Structure

```
Sepsis_Mortality_Prediction_WebApp/
├── SepsisWebApp/              # Flask web application
│   ├── app.py                 # Flask application with REST API
│   ├── main.py                # Model testing script
│   ├── model.pkl              # Trained XGBoost model
│   ├── XGBoost.ipynb          # Model training notebook
│   ├── extractedMimic.csv     # MIMIC-III dataset
│   ├── templates/             # HTML templates
│   └── requirements.txt       # Python dependencies
│
├── streamlit/                 # Streamlit web application
│   └── streamlitProject/
│       ├── app.py             # Main Streamlit application
│       ├── MahyarApp.py       # Alternative Streamlit interface
│       ├── model.pkl          # Trained XGBoost model
│       └── requirements       # Python dependencies
│
└── README.md                  # This file
```

## 🔬 Clinical Features

The model uses the following 11 clinical parameters to predict mortality risk:

| Feature | Description | Type |
|---------|-------------|------|
| **urineoutput** | Urine output in mL | Continuous |
| **lactate_min** | Minimum lactate level | Continuous |
| **bun_mean** | Mean blood urea nitrogen | Continuous |
| **sysbp_min** | Minimum systolic blood pressure | Continuous |
| **metastatic_cancer** | Presence of metastatic cancer | Binary (0/1) |
| **inr_max** | Maximum INR (blood clotting) | Continuous |
| **age** | Patient age in years | Integer |
| **sodium_max** | Maximum sodium level | Continuous |
| **aniongap_max** | Maximum anion gap | Continuous |
| **creatinine_min** | Minimum creatinine level | Continuous |
| **spo2_mean** | Mean oxygen saturation | Continuous |

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip package manager
- Git (for cloning the repository)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ParsaHaghighatgoo/Sepsis_Mortality_Prediction_WebApp.git
   cd Sepsis_Mortality_Prediction_WebApp
   ```

2. **Choose your preferred implementation**

   #### Option A: Flask Application
   ```bash
   cd SepsisWebApp
   pip install flask joblib numpy scikit-learn xgboost
   ```

   #### Option B: Streamlit Application
   ```bash
   cd streamlit/streamlitProject
   pip install streamlit joblib numpy scikit-learn xgboost
   ```

## 💻 Usage

### Flask Application

1. **Start the Flask server**
   ```bash
   cd SepsisWebApp
   python app.py
   ```

2. **Access the application**
   - Open your browser and navigate to `http://localhost:5000`
   - Fill in the patient's clinical parameters
   - Click "Predict" to get the mortality risk assessment

3. **API Endpoint**
   ```bash
   POST /predict
   Content-Type: application/x-www-form-urlencoded
   
   # Form data with all 11 clinical features
   ```

### Streamlit Application

1. **Start the Streamlit server**
   ```bash
   cd streamlit/streamlitProject
   streamlit run app.py
   ```

2. **Access the application**
   - The application will automatically open in your default browser
   - Navigate to `http://localhost:8501` if it doesn't open automatically
   - Enter patient data in the sidebar
   - View real-time predictions and probability scores

### Example Prediction

**Input:**
```python
urineoutput = 35.0
lactate_min = 1.1
bun_mean = 36.5
sysbp_min = 90.0
metastatic_cancer = 0
inr_max = 1.4
age = 56
sodium_max = 143.0
aniongap_max = 18.0
creatinine_min = 5.3
spo2_mean = 95.1
```

**Output:**
- **Prediction**: Low Risk / High Risk
- **Probability**: 0.XXXXX (mortality probability)

## 📊 Model Development

The XGBoost model was developed using:

1. **Dataset**: MIMIC-III Clinical Database
   - 4,555 sepsis patient records
   - Patients aged 18 and above
   - 106 initial features reduced to 11 key predictors

2. **Model Training**: See `XGBoost.ipynb` for:
   - Data preprocessing and feature engineering
   - Feature selection and importance analysis
   - Model training and hyperparameter tuning
   - Performance evaluation and validation

3. **Performance Metrics**: The model achieves competitive performance in predicting sepsis mortality risk

## 🛠️ Technologies Used

- **Machine Learning**: XGBoost, scikit-learn
- **Web Frameworks**: Flask, Streamlit
- **Data Processing**: pandas, numpy
- **Model Persistence**: joblib
- **Data Source**: MIMIC-III Clinical Database

## 📁 Dataset

This project uses the **MIMIC-III (Medical Information Mart for Intensive Care III)** database, which contains de-identified health data from ICU patients. 

> **Note**: Access to MIMIC-III requires completion of the CITI "Data or Specimens Only Research" course and signing a data use agreement.

## 🔒 Important Disclaimers

⚠️ **Medical Disclaimer**: This application is for **research and educational purposes only**. It should NOT be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult qualified healthcare professionals for medical decisions.

⚠️ **Data Privacy**: Ensure compliance with HIPAA and other relevant healthcare data regulations when deploying this application.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is available for educational and research purposes. Please ensure compliance with MIMIC-III data use agreements.

## 👥 Authors

- **Parsa Haghighatgoo** - [ParsaHaghighatgoo](https://github.com/ParsaHaghighatgoo)

## 🙏 Acknowledgments

- MIMIC-III database team at MIT Laboratory for Computational Physiology
- XGBoost development team
- Flask and Streamlit communities

## 📧 Contact

For questions or feedback, please open an issue on GitHub or contact the repository owner.

---

**Built with ❤️ for improving sepsis patient outcomes**