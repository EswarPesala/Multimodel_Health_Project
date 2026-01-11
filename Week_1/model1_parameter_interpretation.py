import pandas as pd

# Load validated & standardized dataset
df = pd.read_csv("../data/validated_standardized_data.csv")

# -----------------------------
# Blood Pressure Interpretation
# -----------------------------
def bp_status(sys, dia):
    if sys < 90 or dia < 60:
        return "Low"
    elif sys <= 120 and dia <= 80:
        return "Normal"
    else:
        return "High"

# -----------------------------
# Cholesterol Interpretation
# -----------------------------
def cholesterol_status(val):
    if val == 1:
        return "Normal"
    elif val == 2:
        return "Above Normal"
    else:
        return "High"

# -----------------------------
# Glucose Interpretation
# -----------------------------
def glucose_status(val):
    if val == 1:
        return "Normal"
    elif val == 2:
        return "Above Normal"
    else:
        return "High"

# Apply Model 1 rules
df["BP_Status"] = df.apply(
    lambda x: bp_status(x["systolic_bp"], x["diastolic_bp"]), axis=1
)

df["Cholesterol_Status"] = df["cholesterol_level"].apply(cholesterol_status)
df["Glucose_Status"] = df["glucose_level"].apply(glucose_status)

# Display sample output
print(df[
    [
        "systolic_bp",
        "diastolic_bp",
        "BP_Status",
        "Cholesterol_Status",
        "Glucose_Status"
    ]
].head())

# Save Model-1 output
df.to_csv("../data/model1_output.csv", index=False)

print("✅ Model 1: Parameter Interpretation completed successfully")
