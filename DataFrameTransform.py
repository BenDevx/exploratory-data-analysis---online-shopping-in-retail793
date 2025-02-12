# TASK 3
import pandas as pd
import matplotlib.pyplot as plt

# The first class is called DataFrameTransform Class
class DataFrameTransform:
    def __init__(self, df):
        self.df = df

    def check_nulls(self):
        """ This checks for missing values in each column and return their count and percentage."""
        null_count = self.df.isnull().sum()
        null_percentage = (null_count / len(self.df)) * 100
        null_info = pd.DataFrame({'Null Count': null_count, 'Percentage': null_percentage})
        return null_info

# The second class is the Plotter Class
class Plotter:
    def __init__(self, df):
        self.df = df

    def plot_nulls(self):
        """ Here visualises missing data with a simple bar chart."""
        null_count = self.df.isnull().sum()
        null_count = null_count[null_count > 0]  # Only show columns with missing data
        null_count.plot(kind='bar', figsize=(12, 6))
        plt.title("Missing Data Count")
        plt.ylabel("Number of NULLs")
        plt.xlabel("Columns")
        plt.show()


# Task 2 Load the cleaned data and 
df_cleaned = pd.read_csv("cleaned_data.csv")

# Initialise classes
df_transform = DataFrameTransform(df_cleaned)
plotter = Plotter(df_cleaned)

# Checks for NULLs and plot the chart
null_info = df_transform.check_nulls()
print(null_info)

# Plot NULLs
plotter.plot_nulls()


'''Determines the amount of NULLs in each column and
Determine which columns should be dropped within 30% threshold'''
import pandas as pd

# DataFrameTransform Class
class DataFrameTransform:
    def __init__(self, df):
        self.df = df

    def check_nulls(self):
        """Check for missing values in each column and return their count and percentage."""
        null_count = self.df.isnull().sum()
        null_percentage = (null_count / len(self.df)) * 100
        null_info = pd.DataFrame({'Null Count': null_count, 'Percentage': null_percentage})
        return null_info

    def drop_columns_with_nulls(self, threshold=30):
        """Drop columns where the percentage of NULL values exceeds the given threshold."""
        null_info = self.check_nulls()
        columns_to_drop = null_info[null_info['Percentage'] > threshold].index
        self.df = self.df.drop(columns=columns_to_drop)
        return self.df


# First, load the cleaned data
df_cleaned = pd.read_csv("cleaned_data.csv")

# Then, initialise the DataFrameTransform class
df_transform = DataFrameTransform(df_cleaned)

# Finally, drop columns with NULL values above 30% threshold
df_cleaned = df_transform.drop_columns_with_nulls(threshold=30)

# Print the updated DataFrame
print(df_cleaned.head())



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


''' Final step(4) Check if all NULL values have been removed and plot to visualise the removal of all NULL values.'''
# Recheck for NULL values after imputation
print(df_cleaned.isnull().sum())

import pandas as pd
import matplotlib.pyplot as plt
df_cleaned = pd.read_csv("cleaned_data.csv")
class Plotter:
    def __init__(self, df):
        self.df = df
        
    def plot_null_values(self):
        null_counts = self.df.isnull().sum()
        null_percentage = (null_counts / len(self.df)) * 100
        
        plt.figure(figsize=(10, 6))
        null_percentage.plot(kind='bar')
        plt.title('Percentage of NULL Values in Each Column')
        plt.xlabel('Columns')
        plt.ylabel('Percentage of NULLs')
        plt.xticks(rotation=90)
        plt.show()

# Initialise Plotter with the cleaned dataset
plotter = Plotter(df_cleaned)

# Visualise the removal of NULL values
plotter.plot_null_values()

''' TASK 4: performing some transformations of skewed colums.'''
# First by identifying the columns with skewness
import pandas as pd
import numpy as np
df_cleaned = pd.read_csv("cleaned_data.csv")
# Identify numeric columns
numeric_cols = df_cleaned.select_dtypes(include=[np.number]).columns

# Compute skewness for each numeric column
skewness = df_cleaned[numeric_cols].skew()

# Set threshold for high skewness (absolute value > 1)
skewed_cols = skewness[abs(skewness) > 1].index.tolist()

# Print skewed columns
print("Skewed Columns:", skewed_cols)

'''This plots a bar chart to view all skewed columns'''
# Import Matplotlib for creating plots
import matplotlib.pyplot as plt  

class Plotter:
    def __init__(self, df):
        """
        The constructor method runs when I create an instance of the class.
        It takes a DataFrame (df) as input and stores it for later use in plotting.
        """
        self.df = df

    def plot_null_values(self):
        """
        Calculates the missing (NULL) values in each column.
        Then, calculates the percentage of missing values relative to the total number of rows and 
        creates a bar chart to show which columns have missing values and how much.
        """
        null_counts = self.df.isnull().sum() 
        null_percentage = (null_counts / len(self.df)) * 100 
        
        plt.figure(figsize=(10, 6)) 
        null_percentage.plot(kind='bar', color='red')
        plt.title('Percentage of NULL Values in Each Column') 
        plt.xlabel('Columns') 
        plt.ylabel('Percentage of NULLs') 
        plt.xticks(rotation=90) 
        plt.show() 

    def plot_skewed_columns(self, columns):
        """
        Takes a list of skewed columns and creates histograms for each.
        If the bars are mostly on one side instead of being evenly spread, the column is skewed.
        """
        plt.figure(figsize=(15, 10)) 
        for i, col in enumerate(columns, 1): 
            plt.subplot(3, 4, i) 
            self.df[col].hist(bins=30, color='blue', alpha=0.7) 
            plt.title(col) 
        plt.tight_layout()
        plt.show() 

# Initialize the Plotter class with our cleaned dataset
plotter = Plotter(df_cleaned)

# List of columns that were identified as skewed earlier
skewed_cols = ['administrative', 'administrative_duration', 'informational', 
               'informational_duration', 'product_related', 'product_related_duration', 
               'bounce_rates', 'exit_rates', 'page_values', 'visitor_type']

# Call the method to visualize the skewed columns
plotter.plot_skewed_columns(skewed_cols)


''' Next is to apply some transformations to identified skewed columns'''
import numpy as np  # Import NumPy for mathematical operations

class DataFrameTransform:
    def __init__(self, df):
        """
        Initializes the class with a DataFrame.
        The DataFrame is stored in self.df, so it can be used in other methods.
        """
        self.df = df

    def transform_skewed_columns(self, columns):
        """
        Reduces skewness in the given columns.
        - If a column has zero or negative values, we use log transformation (`log1p`).
        - Otherwise, we use square root transformation (`sqrt`).
        """
        for col in columns:
            if (self.df[col] <= 0).any():  
                print(f"Applying log transformation to {col} because it contains zero or negative values.")
                self.df[col] = np.log1p(self.df[col])  # Log transformation to handle skewness
            else:
                print(f"Applying square root transformation to {col}.")
                self.df[col] = np.sqrt(self.df[col])  # Square root transformation to reduce skewness

        print("Skewed columns have been transformed.")

# Initialize the class with the cleaned dataset
df_transform = DataFrameTransform(df_cleaned)

# Apply transformations to the identified skewed columns
df_transform.transform_skewed_columns(skewed_cols)

''' Here visualises the columns after applying transformations'''
import matplotlib.pyplot as plt
import seaborn as sns  # Import seaborn for better visualization

class Plotter:
    def __init__(self, df):
        """
        This constructor initializes the class with a DataFrame.
        The DataFrame is stored in self.df, so we can use it for visualization.
        """
        self.df = df

    def plot_skewed_columns(self, columns):
        """
        This function plots histograms of the skewed columns after transformation.
        It helps visualize whether the skewness has been reduced.
        """
        plt.figure(figsize=(15, 10))  # Set the overall figure size

        for i, col in enumerate(columns, 1):  
            plt.subplot(3, 4, i)  # Arrange subplots in a grid
            sns.histplot(self.df[col], bins=30, kde=True)  # Plot histogram with KDE (density curve)
            plt.title(f"Histogram of {col}")  # Add a title
        
        plt.tight_layout()  # Adjust layout to prevent overlapping
        plt.show()  # Display all the plots

# Initialize the class with the transformed dataset
plotter = Plotter(df_transform.df)

# Visualize the transformed skewed columns
plotter.plot_skewed_columns(skewed_cols)

# Saves a copy of the transformed dataset
df_cleaned.to_csv("transformed_data.csv", index=False)
print("Transformed dataset saved as 'transformed_data.csv'.")
