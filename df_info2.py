import pandas as pd
df_cleaned = pd.read_csv("cleaned_data.csv")
print(df_cleaned.head())

# Import Matplotlib for creating plots
import matplotlib.pyplot as plt  

class Plotter:
    def __init__(self, df):
        """
        This is the constructor method that runs when we create an instance of the class.
        It takes a DataFrame (df) as input and stores it for later use in plotting.
        """
        self.df = df

    def plot_null_values(self):
        """
        This function calculates the number of missing (NULL) values in each column.
        Then, it calculates the percentage of missing values relative to the total number of rows.
        It creates a bar chart to show which columns have missing values and how much.
        """
        null_counts = self.df.isnull().sum()  # Count the NULL values in each column
        null_percentage = (null_counts / len(self.df)) * 100  # Convert counts to percentages
        
        plt.figure(figsize=(10, 6))  # Set figure size for better readability
        null_percentage.plot(kind='bar', color='orange')  # Create a bar chart
        plt.title('Percentage of NULL Values in Each Column')  # Set the title of the plot
        plt.xlabel('Columns')  # Label for the x-axis
        plt.ylabel('Percentage of NULLs')  # Label for the y-axis
        plt.xticks(rotation=90)  # Rotate x-axis labels for better visibility
        plt.show()  # Display the plot

    def plot_skewed_columns(self, columns):
        """
        This function takes a list of skewed columns and creates histograms for each.
        A histogram shows how the data is distributed, helping us see if a column is skewed.
        If the bars are mostly on one side instead of being evenly spread, the column is skewed.
        """
        plt.figure(figsize=(15, 10))  # Set a larger figure size so all plots fit properly
        for i, col in enumerate(columns, 1):  # Loop through each column
            plt.subplot(3, 4, i)  # Arrange subplots in a grid (3 rows, 4 columns)
            self.df[col].hist(bins=30, color='blue', alpha=0.7)  # Create a histogram with 30 bins
            plt.title(col)  # Set the title of each subplot to the column name
        plt.tight_layout()  # Adjust layout to prevent overlapping
        plt.show()  # Display the plots

# Initialize the Plotter class with our cleaned dataset
plotter = Plotter(df_cleaned)

# List of columns that were identified as skewed earlier
skewed_cols = ['administrative', 'administrative_duration', 'informational', 
               'informational_duration', 'product_related', 'product_related_duration', 
               'bounce_rates', 'exit_rates', 'page_values', 'visitor_type']

# Call the method to visualize the skewed columns
plotter.plot_skewed_columns(skewed_cols)
