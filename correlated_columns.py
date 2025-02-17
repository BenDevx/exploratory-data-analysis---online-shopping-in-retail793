import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the cleaned dataset
df_cleaned = pd.read_csv("cleaned_data.csv")

# Step 1: Compute and visualise the correlation matrix
def plot_correlation_matrix(df):
    """Compute and visualise the correlation matrix."""
    numeric_df = df.select_dtypes(include=[np.number])  # Keep only numeric columns
    corr_matrix = numeric_df.corr()  # Compute correlation only on numerical data
    
    if corr_matrix.empty:
        print("No numeric columns available for correlation matrix.")
        return

    # Plot the correlation matrix as a heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', vmin=-1, vmax=1)
    plt.title("Correlation Matrix")
    plt.show()

# Step 2: Identify and remove highly correlated columns
def remove_highly_correlated_columns(df, threshold=0.8):
    """Remove columns that are highly correlated above my given threshold."""
    numeric_df = df.select_dtypes(include=[np.number])  # Keep only numeric columns
    corr_matrix = numeric_df.corr()

    if corr_matrix.empty:
        print("No numeric columns available for correlation analysis.")
        return df, []  # Return unchanged dataframe if no numeric data exists

    to_drop = set()
    for col in corr_matrix.columns:
        if col not in to_drop:  # Ensures I don't drop already removed columns
            highly_corr = corr_matrix[col][abs(corr_matrix[col]) > threshold].index.tolist()
            highly_corr.remove(col)  # Remove the column itself
            to_drop.update(highly_corr)  # Add correlated columns to remove list

    to_drop = sorted(to_drop)  # Convert to sorted list for better readability
    df_cleaned_dropped = df.drop(columns=to_drop, errors='ignore')  # Drop with error handling
    return df_cleaned_dropped, to_drop

# Step 3: Apply the function and visualise results
plot_correlation_matrix(df_cleaned)  # Step 1: Visualise correlation matrix
df_cleaned, removed_columns = remove_highly_correlated_columns(df_cleaned, threshold=0.8)  # Step 2: Remove correlated columns

print(f"Removed columns: {removed_columns}")
print(f"Remaining columns: {df_cleaned.columns.tolist()}")

# Save the cleaned dataset
df_cleaned.to_csv("cleaned_data_no_high_corr.csv", index=False)
print("Cleaned dataset with removed highly correlated columns saved as 'cleaned_data_no_high_corr.csv'.")

# Step 4: Remove the 'bounce_rate' column separately
if 'bounce_rate' in df_cleaned.columns:
    df_cleaned = df_cleaned.drop(columns=['bounce_rate'])
    print("Column 'bounce_rate' removed.")

# Save the final dataset after bounce rate removal
df_cleaned.to_csv("cleaned_data_no_bounce_rate.csv", index=False)
print("Final dataset saved as 'cleaned_data_no_bounce_rate.csv'.")
print(f"Final remaining columns: {df_cleaned.columns.tolist()}")
