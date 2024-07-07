import pandas as pd
from dataframe import df1 as df_1

# First 5 rows
print(df_1.head())

# Last 5 rows
print(df_1.tail())

# Summary of the DataFrame
print(df_1.info())

# Statistical summary of numerical columns
print(df_1.describe())