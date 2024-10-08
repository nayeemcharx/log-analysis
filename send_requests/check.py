
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('http_requests_xss.csv')

# Get the number of rows
num_rows = len(df)

print(f'The number of rows in the CSV file is: {num_rows}')
