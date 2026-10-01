import pandas as pd
import numpy as np

# Make results reproducible
np.random.seed(42)

data = []


# ==========================================
# 1. MOSFET - NORMAL
# ==========================================

for _ in range(400):

    voltage = np.random.normal(10, 1.2)
    current = np.random.normal(0.7, 0.25)
    resistance = np.random.normal(5, 1.5)
    temperature = np.random.normal(40, 10)

    data.append([
        "MOSFET",
        voltage,
        current,
        resistance,
        temperature,
        "Normal"
    ])


# ==========================================
# 2. MOSFET - OVERCURRENT
# ==========================================

for _ in range(400):

    voltage = np.random.normal(10, 1.5)
    current = np.random.normal(1.5, 0.45)
    resistance = np.random.normal(5, 1.8)
    temperature = np.random.normal(65, 15)

    data.append([
        "MOSFET",
        voltage,
        current,
        resistance,
        temperature,
        "Overcurrent"
    ])


# ==========================================
# 3. MOSFET - OVERHEATING
# ==========================================

for _ in range(400):

    voltage = np.random.normal(10, 1.3)
    current = np.random.normal(1.1, 0.3)
    resistance = np.random.normal(9, 2)
    temperature = np.random.normal(90, 15)

    data.append([
        "MOSFET",
        voltage,
        current,
        resistance,
        temperature,
        "Overheating"
    ])


# ==========================================
# 4. MOSFET - GATE FAULT
# ==========================================

for _ in range(400):

    voltage = np.random.normal(3, 0.8)
    current = np.random.normal(0.4, 0.2)
    resistance = np.random.normal(18, 4)
    temperature = np.random.normal(50, 12)

    data.append([
        "MOSFET",
        voltage,
        current,
        resistance,
        temperature,
        "Gate Fault"
    ])


# ==========================================
# Create DataFrame
# ==========================================

df = pd.DataFrame(
    data,
    columns=[
        "Component",
        "Voltage",
        "Current",
        "Resistance",
        "Temperature",
        "Fault"
    ]
)


# ==========================================
# Remove impossible negative values
# ==========================================

df["Voltage"] = df["Voltage"].clip(lower=0)
df["Current"] = df["Current"].clip(lower=0)
df["Resistance"] = df["Resistance"].clip(lower=0)
df["Temperature"] = df["Temperature"].clip(lower=0)


# ==========================================
# Save dataset
# ==========================================

df.to_csv(
    "../data/component_fault_dataset.csv",
    index=False
)


# ==========================================
# Display information
# ==========================================

print("Realistic dataset created successfully!")
print()

print("Number of rows:", len(df))
print()

print("Fault distribution:")
print(df["Fault"].value_counts())
print()

print("Dataset statistics:")
print(df.describe())

print()

print("First 5 rows:")
print(df.head())