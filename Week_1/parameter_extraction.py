import pandas as pd

df = pd.read_csv("../data/cardio_train.csv", sep=";")

key_parameters = df[
    ["age", "gender", "ap_hi", "ap_lo", "cholesterol", "gluc"]
]

print(key_parameters.head())
