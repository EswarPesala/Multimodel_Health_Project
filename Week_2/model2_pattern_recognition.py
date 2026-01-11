import pandas as pd

# Load Model-1 output
df = pd.read_csv("../data/model1_output.csv")

print(df.head())


def identify_patterns(row):
    risks = []

    if row["BP_Status"] == "High":
        risks.append("Hypertension Risk")

    if row["Glucose_Status"] == "High":
        risks.append("Diabetes Risk")

    if row["BP_Status"] == "High" and row["Cholesterol_Status"] == "High":
        risks.append("Cardiovascular Risk")

    if row["Glucose_Status"] == "High" and row["BMI"] >= 30:
        risks.append("Metabolic Risk")

    if not risks:
        return "Low Risk"

    return ", ".join(risks)

df["Identified_Risks"] = df.apply(identify_patterns, axis=1)

print(df[["BP_Status", "Cholesterol_Status", "Glucose_Status", "Identified_Risks"]].head())


def risk_score(row):
    score = 0

    if row["BP_Status"] == "High":
        score += 2
    if row["Cholesterol_Status"] == "High":
        score += 2
    if row["Glucose_Status"] == "High":
        score += 2
    if row["BMI"] >= 30:
        score += 1

    return score

df["Risk_Score"] = df.apply(risk_score, axis=1)

print(df[["Identified_Risks", "Risk_Score"]].head())



df.to_csv("../data/model2_output.csv", index=False)
print("✅ Model 2 completed successfully")
