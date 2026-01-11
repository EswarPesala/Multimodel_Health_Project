import pandas as pd

df = pd.read_csv(
    r"C:\To learn\Infosys_Internship_6_0\AI_HEALTH_DIAGNOSTICS\archive_cbc\CBC data_for_meandeley_csv.csv",
    sep=";"
)

print(df.head())
print(df.info())
print(df.describe())

print(df.shape)
