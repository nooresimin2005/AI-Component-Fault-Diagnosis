def generate_troubleshooting(
    component,
    voltage,
    current,
    resistance,
    temperature,
    fault,
    confidence
):
    if fault == "Overcurrent":
        advice = f"""
FAULT: Overcurrent

The ML model predicts an overcurrent condition in the {component}.

Possible causes:
1. Excessive load connected to the component.
2. Short circuit or low-resistance path.
3. Incorrect circuit connection.
4. Component may be damaged.

Recommended checks:
1. Switch off the circuit before inspection.
2. Check the load connected to the component.
3. Measure the resistance across the suspected path.
4. Check whether the current is higher than the expected operating current.
5. Inspect the component for physical damage or overheating.

Suggested action:
Check the load and circuit connections first. If the component is damaged,
replace it after identifying the cause of the excessive current.

Measured values:
Voltage: {voltage} V
Current: {current} A
Resistance: {resistance} Ohm
Temperature: {temperature} °C

ML confidence: {confidence * 100:.2f}%
"""

    elif fault == "Overheating":
        advice = f"""
FAULT: Overheating

The ML model predicts an overheating condition in the {component}.

Possible causes:
1. Excessive current.
2. Poor heat dissipation.
3. Continuous operation under heavy load.
4. Damaged component.

Recommended checks:
1. Check the component temperature.
2. Check the current flowing through the component.
3. Inspect the heat sink or cooling arrangement.
4. Check for abnormal resistance or connections.

Suggested action:
Reduce excessive loading and improve cooling if required.
Inspect the component for possible damage.

Measured temperature: {temperature} °C
Current: {current} A
ML confidence: {confidence * 100:.2f}%
"""

    elif fault == "Gate Fault":
        advice = f"""
FAULT: Gate Fault

The ML model predicts a possible gate-related fault in the {component}.

Possible causes:
1. Incorrect gate/control signal.
2. Gate connection problem.
3. Excessive gate voltage.
4. Damaged component.

Recommended checks:
1. Check the gate/control connection.
2. Measure the control signal.
3. Inspect the gate circuit for loose connections.
4. Check for physical damage.

Suggested action:
Verify the control signal and gate connections before replacing the component.

Voltage: {voltage} V
Current: {current} A
Temperature: {temperature} °C
ML confidence: {confidence * 100:.2f}%
"""

    elif fault == "Normal":
        advice = f"""
STATUS: Normal

The ML model predicts that the {component} is operating under normal
conditions for the supplied measurements.

Recommended checks:
1. Continue monitoring voltage and current.
2. Monitor temperature during operation.
3. Check for sudden changes in measurements.

Measured values:
Voltage: {voltage} V
Current: {current} A
Resistance: {resistance} Ohm
Temperature: {temperature} °C

ML confidence: {confidence * 100:.2f}%
"""

    else:
        advice = f"""
FAULT: {fault}

The ML model detected a possible abnormal condition in the {component}.

Recommended action:
Inspect the circuit connections and verify the measured electrical values.

ML confidence: {confidence * 100:.2f}%
"""

    return advice