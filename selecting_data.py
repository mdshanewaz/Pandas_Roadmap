import pandas as pd
from dataframe import df1 as df_1

# Selecting a column
# print(df_1['name'])

# Selecting multiple columns
# print(df_1[['name', 'age']])

# Selecting row by index
print(df_1.iloc[0])        # By position
print(df_1.loc[0])         # By label

# To learn more visit the link
# https://www.naukri.com/code360/library/difference-between-loc-and-iloc-in-pandas