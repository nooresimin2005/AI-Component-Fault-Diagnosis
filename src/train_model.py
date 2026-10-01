import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

import matplotlib.pyplot as plt
import seaborn as sns


# ==========================================
# 1. Load dataset
# ==========================================

df = pd.read_csv(
    "../data/component_fault_dataset.csv"
)

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)


# ==========================================
# 2. Encode component names
# ==========================================

component_encoder = LabelEncoder()

df["Component_Code"] = component_encoder.fit_transform(
    df["Component"]
)

print("\nComponent encoding:")

for component, code in zip(
    component_encoder.classes_,
    range(len(component_encoder.classes_))
):
    print(component, "->", code)


# ==========================================
# 3. Select input features
# ==========================================

X = df[
    [
        "Component_Code",
        "Voltage",
        "Current",
        "Resistance",
        "Temperature"
    ]
]


# ==========================================
# 4. Select target
# ==========================================

y = df["Fault"]


# ==========================================
# 5. Split dataset
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# ==========================================
# 6. Create Random Forest
# ==========================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# ==========================================
# 7. Train model
# ==========================================

print("\nTraining Random Forest...")

model.fit(
    X_train,
    y_train
)

print("Training completed!")


# ==========================================
# 8. Make predictions
# ==========================================

y_pred = model.predict(X_test)


# ==========================================
# 9. Evaluate model
# ==========================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\n========================================")
print("MODEL PERFORMANCE")
print("========================================")

print(
    f"Accuracy: {accuracy * 100:.2f}%"
)

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred
    )
)


# ==========================================
# 10. Confusion Matrix
# ==========================================

cm = confusion_matrix(
    y_test,
    y_pred
)

labels = model.classes_

plt.figure(
    figsize=(8, 6)
)

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=labels,
    yticklabels=labels
)

plt.xlabel("Predicted Fault")
plt.ylabel("Actual Fault")

plt.title(
    "Confusion Matrix - Random Forest"
)

plt.tight_layout()

plt.savefig(
    "../models/confusion_matrix.png"
)

print("\nConfusion matrix saved successfully!")
print("Location: ../models/confusion_matrix.png")


# ==========================================
# 11. Save model
# ==========================================

joblib.dump(
    model,
    "../models/fault_model.pkl"
)

joblib.dump(
    component_encoder,
    "../models/component_encoder.pkl"
)

print("\nModel saved successfully!")
print("Location: ../models/fault_model.pkl")

print("\nComponent encoder saved successfully!")
print("Location: ../models/component_encoder.pkl")