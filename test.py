import pandas as pd

# Create a sample Pandas DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Convert the DataFrame to JSON with default settings
json_data = df.to_json()
print("JSON with default settings:")
print(json_data)

# Convert the DataFrame to JSON with specific options
json_data = df.to_json(orient='records', lines=True)
print("\nJSON with 'records' orientation and 'lines' format:")
print(json_data)
