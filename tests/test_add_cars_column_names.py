import pandas as pd
import pytest

# Define the test function
def test_cars_data_loading():
    # Define column names
    column_names = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'car name']
    
    # Load the dataset
    cars_data = pd.read_csv('data/auto-mpg-data.txt', sep='\s+', header=None, names=column_names)
    
    # Assert that the dataset is not empty
    assert not cars_data.empty, "The dataset should not be empty."
    
    # Assert that the column names are correctly assigned
    assert list(cars_data.columns) == column_names, "Column names do not match the expected names."
    
    # Assert that the dataset has the correct number of columns
    assert cars_data.shape[1] == len(column_names), "The dataset should have exactly 9 columns."
    
    # Assert that the dataset has rows
    assert cars_data.shape[0] > 0, "The dataset should have at least one row."