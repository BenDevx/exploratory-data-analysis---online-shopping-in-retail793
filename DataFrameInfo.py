# Full script with all the tasks

import pandas as pd

# First task was to load the cleaned dataset
df_cleaned = pd.read_csv("cleaned_data.csv")

class DataFrameInfo:
    def __init__(self, df): # First initialise the class
        self.df = df

    # This method describes all columns and their data types
    def describe_columns(self):
        print("Describing all columns and their data types:")
        print(self.df.dtypes)
        print("\n")

    # This method extracts statistical values (mean, std, median) from numeric columns 
    def statistical_values(self):
        print("Statistical Values for Each Numeric Column:")
        print("Mean:")
        print(self.df.select_dtypes(include=['number']).mean())
        print("\nStandard Deviation:")
        print(self.df.select_dtypes(include=['number']).std())
        print("\nMedian:")
        print(self.df.median(include=['number']).median())
        print("\n")

    # Here, this method extracts a count of distinct values in categorical columns
    def count_distinct_values(self):
        print("Distinct Values in Categorical Columns:")
        categorical_columns = self.df.select_dtypes(include=['object']).columns
        for col in categorical_columns:
            print(f"{col}: {self.df[col].nunique()} distinct values")
        print("\n")

    # This method is to print the shape of the DataFrame
    def print_shape(self):
        print(f"Shape of the DataFrame:\n{self.df.shape}")
        print("\n")

    # While this method provides counts and percentages of NULL values in each column
    def count_null_values(self):
        print("Count and Percentage of NULL Values in Each Column:")
        null_counts = self.df.isnull().sum()
        null_percentage = (null_counts / len(self.df)) * 100
        for col in self.df.columns:
            print(f"{col}: Count = {null_counts[col]}, Percentage = {null_percentage[col]:.2f}%")
        print("\n")


# Then instantiate the class with the cleaned data
df_info = DataFrameInfo(df_cleaned)

# Calling each method one by one
df_info.describe_columns()            
df_info.statistical_values()         
df_info.count_distinct_values()     
df_info.count_null_values()          
