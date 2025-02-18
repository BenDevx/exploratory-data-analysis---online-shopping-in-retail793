# Question 1: Visualise what traffic is currently generating the most revenue broken down by region

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("cleaned_data_no_bounce_rate.csv")

# Group by region and traffic type to sum up the revenue
revenue_by_traffic_region = df.groupby(['region', 'traffic_type'])['revenue'].sum().reset_index()

# Create a bar plot for revenue by traffic type and region
plt.figure(figsize=(10, 6))
sns.barplot(x='revenue', y='region', hue='traffic_type', data=revenue_by_traffic_region)
plt.title('Revenue by Traffic Type and Region')
plt.xlabel('Total Revenue')
plt.ylabel('Region')
plt.show()

# Question 2: What traffic has the highest bounce rate? 
# This could indicate that the marketing channels advertisement isn't enticing enough for the customers. 
# Conversely a low bounce rate can indicate that the strategy is highly effective. 
# Break down this data by region.

# Group by region and traffic type to get the average bounce rate
bounce_rate_by_traffic_region = df.groupby(['region', 'traffic_type'])['bounce_rates'].mean().reset_index()

# Create a bar plot for bounce rate by traffic type and region
plt.figure(figsize=(10, 6))
sns.barplot(x='bounce_rates', y='region', hue='traffic_type', data=bounce_rate_by_traffic_region)
plt.title('Bounce Rate by Traffic Type and Region')
plt.xlabel('Average Bounce Rate')
plt.ylabel('Region')
plt.show()

# Question 3: Check what months have generated the most sales from ads traffic

# Filter dataset for ad traffic
ads_data = df[df['traffic_type'] == 'Ads']

# Group by month and sum the revenue
revenue_by_month = ads_data.groupby('month')['revenue'].sum().reset_index()

# Create a bar plot for revenue by month
plt.figure(figsize=(10, 6))
sns.barplot(x='month', y='revenue', data=revenue_by_month)
plt.title('Revenue from Ads Traffic by Month')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.show()

