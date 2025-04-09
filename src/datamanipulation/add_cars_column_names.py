import pandas as pd

# Define column names
column_names = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'car name']

# Import the dataset and assign column names
cars_data = pd.read_csv('data/auto-mpg-data.txt', sep='\s+', header=None, names=column_names)

# Display the first few rows of the dataset
print(cars_data.head().to_string())