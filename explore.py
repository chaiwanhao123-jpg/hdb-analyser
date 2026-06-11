import pandas as pd

df = pd.read_csv("resale-flat-prices.csv")
print(df.shape)
print(df.columns.tolist())
print(df.head())
print(df.describe())

print(df[['flat_model', 'flat_type']])