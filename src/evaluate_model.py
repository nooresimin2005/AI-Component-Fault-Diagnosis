import joblib
import pandas as pd
from pathlib import Path
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(BASE_DIR / "models" / "fault_model.pkl")
encoder = joblib.load(BASE_DIR / "models" / "component_encoder.pkl")

data = pd.read_csv(BASE_DIR / "data" / "component_fault_dataset.csv")

data["Component_Code"] = encoder.transform(data["Component"])

X = data[
    [
        "Component_Code",
        "Voltage",
        "Current",
        "Resistance",
        "Temperature"
    ]
]

y = data["Fault"]

predictions = model.predict(X)

accuracy = accuracy_score(y, predictions)

print("=" * 50)
print("MODEL EVALUATION")
print("=" * 50)

print(f"\nAccuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y, predictions))

print("Confusion Matrix:")
print(confusion_matrix(y, predictions))