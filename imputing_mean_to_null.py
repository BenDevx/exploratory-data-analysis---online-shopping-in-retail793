''' Here determines which columns should be imputed with mean, median or mode and print to check values.'''
import pandas as pd

class DataFrameTransform:
    def __init__(self, df):
        self.df = df

    def impute_missing_values(self):
        """ Impute missing values in numerical and categorical columns."""
        
        # Handle numerical columns first
        for column in self.df.select_dtypes(include=['number']).columns:
            if self.df[column].isnull().sum() > 0:
                if self.df[column].skew() > 1:
                    self.df[column] = self.df[column].fillna(self.df[column].median())  # Use median
                else:
                    self.df[column] = self.df[column].fillna(self.df[column].mean())  # Use mean

        # Then handle categorical columns (fill with most frequent value)
        for column in self.df.select_dtypes(include=['object']).columns:
            if self.df[column].isnull().sum() > 0:
                self.df[column] = self.df[column].fillna(self.df[column].mode()[0])

        return self.df

# Load the dataset
df_cleaned = pd.read_csv("cleaned_data.csv")

# Initialise the class
df_transform = DataFrameTransform(df_cleaned)

# Impute missing values
df_cleaned = df_transform.impute_missing_values()

# Check if NULL values are removed
print(df_cleaned.isnull().sum())
