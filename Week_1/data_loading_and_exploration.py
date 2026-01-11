import pandas as pd

df = pd.read_csv(
    r"C:\Users\pilla\OneDrive\Desktop\Multi-Model-AI-Agent\data\cardio_train.csv",
    sep=";"
)

print(df.head())
print(df.info())
print(df.describe())
print(df.shape)