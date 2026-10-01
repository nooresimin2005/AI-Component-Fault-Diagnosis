import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(BASE_DIR / "models" / "fault_model.pkl")
encoder = joblib.load(BASE_DIR / "models" / "component_encoder.pkl")


def predict_fault(component, voltage, current, resistance, temperature):

    component_code = encoder.transform([component])[0]

    data = pd.DataFrame(
        [[component_code, voltage, current, resistance, temperature]],
        columns=[
            "Component_Code",
            "Voltage",
            "Current",
            "Resistance",
            "Temperature"
        ]
    )

    prediction = model.predict(data)[0]

    probabilities = model.predict_proba(data)[0]

    confidence = max(probabilities)

    probability_dict = dict(
        zip(model.classes_, probabilities)
    )

    return prediction, confidence, probability_dict