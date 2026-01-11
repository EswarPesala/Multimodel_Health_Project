import pandas as pd

# Load Model-2 output
df = pd.read_csv("../data/model2_output.csv")

# -----------------------------
# Create Test Set (20 samples)
# -----------------------------
test_df = df.sample(20, random_state=42)

# -----------------------------
# Expected Pattern Logic
# -----------------------------
def expected_patterns(row):
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

test_df["Expected_Risks"] = test_df.apply(expected_patterns, axis=1)

# -----------------------------
# Pattern Identification Accuracy
# -----------------------------
test_df["Pattern_Match"] = test_df["Expected_Risks"] == test_df["Identified_Risks"]
pattern_accuracy = test_df["Pattern_Match"].mean() * 100

print("Pattern Identification Accuracy:", pattern_accuracy, "%")

# -----------------------------
# Risk Score Plausibility Check
# -----------------------------
def risk_score_plausible(row):
    expected_score = 0

    if row["BP_Status"] == "High":
        expected_score += 2
    if row["Cholesterol_Status"] == "High":
        expected_score += 2
    if row["Glucose_Status"] == "High":
        expected_score += 2
    if row["BMI"] >= 30:
        expected_score += 1

    return row["Risk_Score"] >= expected_score

test_df["Risk_Plausible"] = test_df.apply(risk_score_plausible, axis=1)
risk_plausibility = test_df["Risk_Plausible"].mean() * 100

print("Risk Score Plausibility:", risk_plausibility, "%")

# -----------------------------
# Save evaluation results
# -----------------------------
test_df.to_csv("evaluation_results.csv", index=False)

print("✅ Milestone-2 Evaluation Completed Successfully")
