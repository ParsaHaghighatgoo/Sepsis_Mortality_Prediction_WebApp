from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the saved model
model = joblib.load('model.pkl')


@app.route('/')
def index():
    return render_template('index.html')  # Render the frontend


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the request
        data = request.form  # From the HTML form
        features = [
            float(data['urineoutput']),
            float(data['lactate_min']),
            float(data['bun_mean']),
            float(data['sysbp_min']),
            int(data['metastatic_cancer']),
            float(data['inr_max']),
            float(data['age']),
            float(data['sodium_max']),
            float(data['aniongap_max']),
            float(data['creatinine_min']),
            float(data['spo2_mean'])
        ]

        # Prepare input for prediction
        input_data = np.array(features).reshape(1, -1)

        # Make prediction
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]

        return jsonify({
            'prediction': int(prediction),
            'probability': float(probability)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
