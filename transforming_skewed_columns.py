import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Identify and transform skewed columns
class DataFrameTransform:
    def __init__(self, df):
        """Initialise with a DataFrame."""
        self.df = df

    def identify_skewed_columns(self, threshold=1):
        """Find columns with skewness above the given threshold."""
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        skewness = self.df[numeric_cols].skew()
        skewed_cols = skewness[abs(skewness) > threshold].index.tolist()
        print("Skewed Columns:", skewed_cols)
        return skewed_cols

    def transform_skewed_columns(self, columns):
        """Apply transformations to reduce skewness. Log transformation is used for positive values,
        while square root transformation is applied otherwise.
        """
        for col in columns:
            if (self.df[col] > 0).all():  # Apply log transformation if all values are positive
                self.df[col] = np.log1p(self.df[col])  
            else:  # Apply square root transformation, shifting if necessary
                shift = abs(self.df[col].min()) + 1 if self.df[col].min() <= 0 else 0
                self.df[col] = np.sqrt(self.df[col] + shift)
                
        print("Skewed columns have been transformed.")
        return self.df

# Step 2: Visualise skewed columns before transformation
class Plotter:
    def __init__(self, df):
        """Initialise with the DataFrame."""
        self.df = df

    def plot_skewed_columns(self, columns):
        """Plot histograms of skewed columns to visualise their distributions before and after transformation."""
        if not columns:
            print("No skewed columns to visualise.")
            return
        
        plt.figure(figsize=(12, 8))
        for i, col in enumerate(columns, 1):
            plt.subplot(3, 4, i)
            sns.histplot(self.df[col], bins=30, kde=True)
            plt.title(col)
        plt.tight_layout()
        plt.show()

# Step 3: Visualise after transformation
# Step 4: Save transformed data
if __name__ == "__main__":
    # Load data
    df_cleaned = pd.read_csv("cleaned_data.csv")
    
    # Identify skewed columns
    transform = DataFrameTransform(df_cleaned)
    skewed_cols = transform.identify_skewed_columns()  # This returns the skewed columns list
    
    if skewed_cols:  # Check if there are any skewed columns before attempting to plot and transform
        # Visualise before transformation
        plotter = Plotter(df_cleaned)
        plotter.plot_skewed_columns(skewed_cols)
        
        # Transform skewed columns
        df_cleaned = transform.transform_skewed_columns(skewed_cols)
        
        # Visualise after transformation
        plotter.plot_skewed_columns(skewed_cols)
        
        # Save transformed dataset
        df_cleaned.to_csv("transformed_data.csv", index=False)
        print("Transformed dataset saved as 'transformed_data.csv'.")
    else:
        print("No skewed columns found that exceed the threshold.")
