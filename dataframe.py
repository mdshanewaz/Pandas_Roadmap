import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'Dulal', 'Habib', 'Taheri', 'Noman', 'Aziz', 'Benjir', 'Harun'],
    'age': [25, 30, 35, 70, 38, 42, 22, 67, 55, 45]
}
df1 = pd.DataFrame(data)
# print(df1)


# Creating a DataFrame from a list of dictionaries
data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 35}
]
df2 = pd.DataFrame(data)
# print(df2)