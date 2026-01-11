import pandas as pd

# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv("../data/cardio_train.csv", sep=";")
print("Initial dataset shape:", df.shape)

# -----------------------------
# 2. AGE STANDARDIZATION
# Convert age from days to years
# -----------------------------
df["age_years"] = (df["age"] / 365).astype(int)

# Remove invalid ages
df = df[(df["age_years"] >= 18) & (df["age_years"] <= 100)]

# -----------------------------
# 3. BLOOD PRESSURE VALIDATION
# -----------------------------
df = df[(df["ap_hi"] >= 80) & (df["ap_hi"] <= 200)]
df = df[(df["ap_lo"] >= 50) & (df["ap_lo"] <= 130)]

# -----------------------------
# 4. HEIGHT & WEIGHT VALIDATION
# -----------------------------
df = df[(df["height"] >= 120) & (df["height"] <= 220)]
df = df[(df["weight"] >= 30) & (df["weight"] <= 200)]

# -----------------------------
# 5. BMI STANDARDIZATION
# -----------------------------
df["BMI"] = df["weight"] / ((df["height"] / 100) ** 2)

# -----------------------------
# 6. VALIDATE CATEGORICAL VALUES
# -----------------------------
df = df[df["cholesterol"].isin([1, 2, 3])]
df = df[df["gluc"].isin([1, 2, 3])]
df = df[df["gender"].isin([1, 2])]
df = df[df["smoke"].isin([0, 1])]
df = df[df["alco"].isin([0, 1])]
df = df[df["active"].isin([0, 1])]

# -----------------------------
# 7. DROP UNUSED COLUMNS
# -----------------------------
df.drop(columns=["id", "age"], inplace=True)

# -----------------------------
# 8. RENAME COLUMNS (STANDARD NAMES)
# -----------------------------
df.rename(columns={
    "ap_hi": "systolic_bp",
    "ap_lo": "diastolic_bp",
    "gluc": "glucose_level",
    "cholesterol": "cholesterol_level"
}, inplace=True)

# -----------------------------
# 9. SAVE CLEANED DATASET
# -----------------------------
df.to_csv("../data/validated_standardized_data.csv", index=False)

print("Final dataset shape:", df.shape)
print("✅ Data Validation & Standardization Completed Successfully")
