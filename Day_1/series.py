import pandas as pd

data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print(series)

series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
print(series)