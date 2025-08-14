import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load custom dataset
file_path = 'data/custom_nids_dataset.csv'
df = pd.read_csv(file_path)

features = ['duration','src_bytes','dst_bytes','wrong_fragment','urgent',
            'hot','num_failed_logins','logged_in','count','srv_count']
X = df[features]
y = df['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'model/rf_model.pkl')

# Print accuracy
print(f"Model training accuracy: {model.score(X_test, y_test):.4f}")
