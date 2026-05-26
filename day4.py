import pandas as pd

# Sample DataFrame
data = {

    'Name': ['Asha', 'Ravi', 'Kiran'],
    'Age': [20, 21, 22],
    'Marks': [85.5, 90.0, 88.5],
    'Passed': [True, True, False]
}

df = pd.DataFrame(data)

# Check datatypes of all columns
print(df.dtypes)

# Select only integer columns
int_columns = df.select_dtypes(include='int')
print("\nInteger Columns:")
print(int_columns)

# Select only object (string) columns
object_columns = df.select_dtypes(include='object')
print("\nObject Columns:")
print(object_columns)

# Select only float columns
float_columns = df.select_dtypes(include='float')
print("\nFloat Columns:")
print(float_columns)