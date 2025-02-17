import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("transformed_data.csv")

# Step 1: Visualise data before removing outliers
def plot_data(df):
    """Plot histograms and boxplots to visualise data distributions and outliers."""
    plt.figure(figsize=(12, 8))
    for i, col in enumerate(df.select_dtypes(include=['number']).columns, 1):
        plt.subplot(3, 4, i)
        sns.histplot(df[col], kde=True)
        plt.title(f"Histogram of {col}")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(12, 8))
    for i, col in enumerate(df.select_dtypes(include=['number']).columns, 1):
        plt.subplot(3, 4, i)
        sns.boxplot(x=df[col])  
        plt.title(f"Boxplot of {col}")
    plt.tight_layout()
    plt.show()

# Step 2: Identify and remove outliers using IQR
def remove_outliers(df):
    """Remove rows with outliers using the IQR method."""
    num_cols = df.select_dtypes(include=['number']).columns
    Q1 = df[num_cols].quantile(0.25)
    Q3 = df[num_cols].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Ensure boolean filtering is applied
    outliers = (df[num_cols] < lower_bound) | (df[num_cols] > upper_bound)
    df_no_outliers = df[~outliers.any(axis=1)].copy()  # .copy() is used to avoid modifying original DataFrame
    return df_no_outliers

# Step 3: Visualise data after removing outliers
plot_data(df)  # Before removing outliers
df_cleaned = remove_outliers(df)
plot_data(df_cleaned)  # After removing outliers

# Step 4: Save the transformed dataset
df_cleaned.to_csv("transformed_data_no_outliers.csv", index=False)
print("Transformed dataset with no outliers saved as 'transformed_data_no_outliers.csv'.")
