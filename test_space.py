import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

# Load transformed dataset
df = pd.read_csv("transformed_data.csv")

# Plot scatter matrix for all numerical columns
scatter_matrix(df, figsize=(12, 12), diagonal='kde', alpha=0.5)

# Show the plot
plt.show()

