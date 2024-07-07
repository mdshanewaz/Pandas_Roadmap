import os
import pandas as pd

data = pd.read_csv('atm_transactions.csv')

# print(data)

# print(data.head())

# print(data.tail())

print(data.info())

df = data[['atmId', 'atmName', 'atmCity', 'totalBalance']]

print(df)

print(df.boxplot)

