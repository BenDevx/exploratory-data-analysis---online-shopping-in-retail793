import pandas as pd

class DataTransform:
    def __init__(self, df):
        """Save the DataFrame."""
        self.df = df.copy()  # Make a new copy to avoid modifying the original

    def convert_to_datetime(self, column):
        """Change a column to datetime format."""
        if column in self.df.columns:
            self.df[column] = pd.to_datetime(self.df[column], errors='coerce')

    def convert_to_category(self, column):
        """Change a column to a category."""
        if column in self.df.columns:
            self.df[column] = self.df[column].astype('category')

    def convert_to_numeric(self, column):
        """Change a column to a number, setting errors to NaN."""
        if column in self.df.columns:
            self.df[column] = pd.to_numeric(self.df[column], errors='coerce')

    def transform(self):
        """Apply all changes."""
        # Convert these columns to category
        for col in ['month', 'weekend', 'revenue']:
            self.convert_to_category(col)

        # Convert these columns to numbers
        for col in ['product_related_duration', 'administrative_duration']:
            self.convert_to_numeric(col)

        print("Data transformation complete.")
        return self.df  # Return the updated DataFrame

    def show_column_types(self):
        """Print the data types of all columns after transformation."""
        print("\nColumn Data Types After Transformation:")
        print(self.df.dtypes)


df = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar'],
    'weekend': [1, 0, 1],
    'revenue': [0, 1, 0],
    'product_related_duration': ['10', '20', '30'],
    'administrative_duration': ['5', '15', '25']
})

# Here creates an instance of DataTransform
transformer = DataTransform(df)

# Apply transformations
df_transformed = transformer.transform()

# Show the first few rows
print("\nTransformed DataFrame:")
print(df_transformed.head())

# Show the updated column types
transformer.show_column_types()
