import pandas as pd
import matplotlib.pyplot as plt

# DataFrameTransform Class
class DataFrameTransform:
    def __init__(self, df):
        """Initialize with a DataFrame."""
        self.df = df

    def check_nulls(self):
        """Check for missing values in each column and return their count and percentage."""
        null_count = self.df.isnull().sum()
        null_percentage = (null_count / len(self.df)) * 100
        null_info = pd.DataFrame({'Null Count': null_count, 'Percentage': null_percentage})
        return null_info

    def drop_columns_with_nulls(self, threshold=30):
        """Drop columns where the percentage of NULL values exceeds my 30% threshold."""
        null_info = self.check_nulls()
        columns_to_drop = null_info[null_info['Percentage'] > threshold].index.tolist()
        self.df.drop(columns=columns_to_drop, inplace=True)  
        return self.df


# First, load the cleaned data
df_cleaned = pd.read_csv("cleaned_data.csv")

# Then, initialise the DataFrameTransform class
df_transform = DataFrameTransform(df_cleaned)

# Finally, drop columns with NULL values above 30% threshold
df_cleaned = df_transform.drop_columns_with_nulls(threshold=30)

# Print the updated DataFrame
print(df_cleaned.head())


# Plotter Class for Visualizing Missing Values
class Plotter:
    def __init__(self, df):
        """Initialize with a DataFrame."""
        self.df = df

    def plot_nulls(self):
        """Visualizes missing data with a bar chart, only showing columns with NULL values."""
        null_count = self.df.isnull().sum()
        null_count = null_count[null_count > 0]  # Only show columns with missing data
        if not null_count.empty:
            null_count.plot(kind='bar', figsize=(12, 6))
            plt.title("Missing Data Count")
            plt.ylabel("Number of NULLs")
            plt.xlabel("Columns")
            plt.show()
        else:
            print("No missing values to visualize.")

# Instantiate and plot missing values
plotter = Plotter(df_cleaned)
plotter.plot_nulls()
