import pandas as pd

df = pd.read_csv('D:\Resume\selected.csv', usecols=[0,4])
# print(df)

print("head",df.head())
print("tail",df.tail())
print(df.to_string())

print(df)