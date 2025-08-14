# Add before any other imports
import numpy as np
np.obj2sctype = lambda obj: np.dtype(obj).type  # Fix NumPy 2.x compatibility

# Then import other modules
import shap
from flask import Flask, request, render_template
# ... rest of your code

from flask import Flask, request, render_template
import joblib
import pandas as pd
import shap

app = Flask(__name__)

# Load the trained model
model = joblib.load("model/rf_model.pkl")

# Features used in the model
features = ['duration','src_bytes','dst_bytes','wrong_fragment','urgent',
            'hot','num_failed_logins','logged_in','count','srv_count']

# Thresholds for features (example values, adjust as needed)
thresholds = {
    'duration': 10000,
    'src_bytes': 1000000,
    'dst_bytes': 1000000,
    'wrong_fragment': 3,
    'urgent': 1,
    'hot': 5,
    'num_failed_logins': 3,
    'logged_in': 1,
    'count': 100,
    'srv_count': 50
}

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', thresholds=thresholds)

@app.route('/predict', methods=['POST'])
def predict():
    input_data = [float(request.form[feature]) for feature in features]
    input_df = pd.DataFrame([input_data], columns=features)

    # Prediction
    prediction = int(model.predict(input_df)[0])

    # SHAP explanation
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(input_df)
    # For binary classification, shap_values is a list
    shap_contrib = shap_values[1][0] if isinstance(shap_values, list) else shap_values[0]

    contribution = dict(zip(features, shap_contrib))

    # Check thresholds
    alerts = {feature: (input_df[feature].values[0] > thresholds[feature]) for feature in features}

    return render_template('results.html', prediction=prediction, contribution=contribution, alerts=alerts)

if __name__ == '__main__':
    app.run(debug=True)
