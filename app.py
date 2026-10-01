import streamlit as st
import pandas as pd

from src.predict import predict_fault
from src.troubleshooter import generate_troubleshooting


st.set_page_config(
    page_title="AI Component Fault Diagnosis",
    page_icon="🔧",
    layout="wide"
)

st.title("🔧 AI-Based Electronic Component Fault Diagnosis")
st.caption("Machine Learning Fault Detection with AI-Assisted Troubleshooting")

st.divider()

# Diagnosis history
if "history" not in st.session_state:
    st.session_state.history = []


# ---------------- INPUT SECTION ----------------

st.header("📥 Component Measurements")

col1, col2 = st.columns(2)

with col1:
    component = st.selectbox(
        "Electronic Component",
        ["MOSFET", "Diode", "Resistor", "Capacitor", "BJT"]
    )

    voltage = st.number_input(
        "Voltage (V)",
        min_value=0.0,
        value=10.0
    )

    current = st.number_input(
        "Current (A)",
        min_value=0.0,
        value=0.5
    )

with col2:
    resistance = st.number_input(
        "Resistance (Ohm)",
        min_value=0.0,
        value=5.0
    )

    temperature = st.number_input(
        "Temperature (°C)",
        value=30.0
    )


st.divider()


# ---------------- DIAGNOSIS ----------------

if st.button("🔍 Diagnose Component", use_container_width=True):

    fault, confidence, probabilities = predict_fault(
        component,
        voltage,
        current,
        resistance,
        temperature
    )

    # Save diagnosis
    st.session_state.history.append({
        "Component": component,
        "Voltage (V)": voltage,
        "Current (A)": current,
        "Resistance (Ω)": resistance,
        "Temperature (°C)": temperature,
        "Predicted Fault": fault,
        "Confidence (%)": round(confidence * 100, 2)
    })


    # ---------------- RESULT ----------------

    st.header("🎯 Diagnosis Result")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Predicted Fault",
            fault
        )

    with col2:
        st.metric(
            "Model Confidence",
            f"{confidence * 100:.2f}%"
        )


    # ---------------- PROBABILITY ----------------

    st.subheader("📈 Fault Probability")

    probability_data = {
        fault_name: probability * 100
        for fault_name, probability in probabilities.items()
    }

    st.bar_chart(probability_data)


    st.divider()


    # ---------------- MEASUREMENTS ----------------

    st.header("📊 Measured Parameters")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Voltage", f"{voltage} V")
    c2.metric("Current", f"{current} A")
    c3.metric("Resistance", f"{resistance} Ω")
    c4.metric("Temperature", f"{temperature} °C")


    st.divider()


    # ---------------- TROUBLESHOOTING ----------------

    st.header("🛠️ AI-Assisted Troubleshooting")

    advice = generate_troubleshooting(
        component,
        voltage,
        current,
        resistance,
        temperature,
        fault,
        confidence
    )

    st.info(advice)


    st.divider()


    # ---------------- SAFETY ----------------

    st.warning(
        "⚠️ Safety: Switch off and isolate the circuit before performing "
        "physical measurements or replacing electronic components."
    )


# ---------------- HISTORY ----------------

st.divider()

st.header("📋 Diagnosis History")

if st.session_state.history:

    history_df = pd.DataFrame(st.session_state.history)

    st.dataframe(
        history_df,
        use_container_width=True
    )

else:

    st.info("No diagnosis history yet.")


# ---------------- MODEL PERFORMANCE ----------------

st.divider()

st.header("📊 Model Performance")

st.metric(
    "Model Accuracy",
    "98.44%"
)

st.write(
    "Classification performance on the generated 1,600-sample dataset:"
)

performance = {
    "Fault": [
        "Gate Fault",
        "Normal",
        "Overcurrent",
        "Overheating"
    ],
    "Precision": [
        1.00,
        0.98,
        0.97,
        0.98
    ],
    "Recall": [
        1.00,
        0.98,
        0.97,
        0.99
    ],
    "F1-Score": [
        1.00,
        0.98,
        0.97,
        0.99
    ]
}

performance_df = pd.DataFrame(performance)

st.dataframe(
    performance_df,
    use_container_width=True,
    hide_index=True
)

st.caption(
    "Performance is measured on the generated dataset. "
    "Real-world hardware validation is required for deployment."
)


# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "AI-Based Electronic Component Fault Diagnosis System | "
    "Random Forest + AI-Assisted Troubleshooting"
)