import pandas as pd

df = pd.read_csv("../data/model2_output.csv")

def adjust_risk(row):
    score = row["Risk_Score"]

    if row["age_years"] >= 50:
        score += 1
    if row["gender"] == 1:  # male
        score += 1
    if row["smoke"] == 1:
        score += 1
    if row["active"] == 0:
        score += 1

    return score

df["Adjusted_Risk_Score"] = df.apply(adjust_risk, axis=1)

print(df[["Risk_Score", "Adjusted_Risk_Score"]].head())

df.to_csv("../data/model3_output.csv", index=False)

print("✅ Model 3 completed successfully")