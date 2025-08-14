# Network Intrusion Detection System (NIDS) 🚦

A colorful, interactive Flask web application for detecting network intrusions using machine learning.  
This project uses a Random Forest classifier trained on a custom dataset with 10 key network features, and provides real-time predictions, feature contribution explanations (using SHAP), and threshold-based alerts for each input.

---

## Features

- **10 Key Network Inputs:** Only the most relevant features for simplicity and speed.
- **Attack/Normal Prediction:** Instantly classifies input as an attack or normal traffic.
- **Threshold Alerts:** Highlights when any feature exceeds a typical "normal" value.
- **Feature Importance:** Shows which features contributed most to the prediction.
- **Interactive & Colorful UI:** Built with Bootstrap for a modern look.

---


## Getting Started

### 1. Clone the Repository

git clone https://github.com/ctrl-piyush/Network-Intrusion-Detection-System-NIDS.git
cd Network-Intrusion-Detection-System-NIDS

### 2. Set Up the Virtual Environment

python -m venv nids_env

On Windows:
nids_env\Scripts\activate

On Mac/Linux:
source nids_env/bin/activate

### 3. Install Requirements

pip install -r requirements.txt

### 4. (Optional) Generate Dataset and Train Model

If you want to recreate the dataset/model:
python data_preprocessing.py
python train_model.py

### 5. Run the App

python app.py

Open your browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## Usage

1. Enter values for the 10 network features.
2. The app will:
   - Predict if the input is an attack or normal.
   - Show which features contributed most to the prediction.
   - Alert you if any input exceeds its normal threshold.

---

## Project Structure

.
├── app.py

├── data_preprocessing.py

├── train_model.py

├── requirements.txt

├── data/

│ └── custom_nids_dataset.csv

├── model/

│ └── rf_model.pkl

└── templates/

├── index.html

└── results.html


---

## Requirements

- Python 3.10+
- See `requirements.txt` for full package list

---

## License

This project is licensed under the MIT License.

---

## Acknowledgments

- [NSL-KDD Dataset](https://www.unb.ca/cic/datasets/nsl.html)
- [SHAP](https://github.com/slundberg/shap)
- [Scikit-learn](https://scikit-learn.org/)

---

## Author

- [ctrl-piyush](https://github.com/ctrl-piyush)

