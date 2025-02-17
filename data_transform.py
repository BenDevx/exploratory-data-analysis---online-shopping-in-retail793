import pandas as pd

class DataTransform:
    def __init__(self, df):
        self.df = df  # Store the DataFrame

    def convert_to_datetime(self, column):
        """Convert a column to datetime format."""
        self.df[column] = pd.to_datetime(self.df[column], errors='coerce')

    def convert_to_category(self, column):
        """Convert a column to a categorical data type."""
        self.df[column] = self.df[column].astype('category')

    def convert_to_numeric(self, column):
        """Convert a column to numeric format """
        self.df[column] = pd.to_numeric(self.df[column])

    def transform(self):
        """Apply transformations to specific columns."""
        if 'month' in self.df.columns:
            self.convert_to_category('month')

        if 'weekend' in self.df.columns:
            self.convert_to_category('weekend')

        if 'revenue' in self.df.columns:
            self.convert_to_category('revenue')

        if 'product_related_duration' in self.df.columns:
            self.convert_to_numeric('product_related_duration')

        if 'administrative_duration' in self.df.columns:
            self.convert_to_numeric('administrative_duration')

        print("Data transformation complete.")

        return self.df  # Return the transformed DataFrame
