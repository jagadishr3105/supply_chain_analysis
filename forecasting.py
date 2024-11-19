# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# +
# Step 1: Load the Excel file 

#Load the data using pandas libary to load the csv file into data frame for analysis 
import pandas as pd

# Load the Excel file into a DataFrame
file_path = "/Users/jagadish/Desktop/Supply chain datasets/supply chain logisitcs problem.xlsx"
df = pd.read_excel(file_path)

# Display the first few rows of the DataFrame
print(df.head())


# +
# STEP 2: EXPLORE THE DATA

# Check the structure of the dataset
print(df.info())  #Data types and null values 
# -

# Summary Statistics 
print(df.describe())

# Check for missing values 
print(df.isnull())

# +
# Step 3 : Clean the Data 

# Remove Duplicates
df = df.drop_duplicates()

# Fill or drop Missing Values
df = df.fillna(0)  # Meaning Replace NaN values with 0

# or
df= df.dropna() # Drop rows with NaN values
# -


