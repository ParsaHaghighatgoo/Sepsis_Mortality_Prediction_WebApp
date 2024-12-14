import joblib

loaded_model = joblib.load('model.pkl')  # Load the model
# Based on your model code, your features are:
#
# urineoutput
# lactate_min
# bun_mean
# sysbp_min
# metastatic_cancer
# inr_max
# age
# sodium_max
# aniongap_max
# creatinine_min
# spo2_mean

input_data = [35, 4.8, 55, 83, 0, 3.7, 53, 135, 42, 4.5, 94]
input_data2 = [35, 1.1, 36.5, 90, 0, 1.4, 56, 143, 18, 5.3, 95.096774]
prediction = loaded_model.predict([input_data2])  # Use the model
print(prediction)
