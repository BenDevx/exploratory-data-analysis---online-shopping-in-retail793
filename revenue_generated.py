# Question 1: Which region is currently generating the most/least revenue?

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('cleaned_data_no_bounce_rate.csv')

# Group by region and sum the revenue
revenue_by_region = df.groupby('region')['revenue'].sum().reset_index()

# Sort by revenue in descending order
revenue_by_region_sorted = revenue_by_region.sort_values(by='revenue', ascending=False)

# Create a bar plot for revenue by region
plt.figure(figsize=(10, 6))
sns.barplot(x='revenue', y='region', data=revenue_by_region_sorted)
plt.title('Revenue by Region')
plt.xlabel('Total Revenue')
plt.ylabel('Region')
plt.show()

# Report the most and least revenue-generating regions
most_revenue_region = revenue_by_region_sorted.iloc[0]
least_revenue_region = revenue_by_region_sorted.iloc[-1]
print(f"Most Revenue Region: {most_revenue_region['region']} - ${most_revenue_region['revenue']}")
print(f"Least Revenue Region: {least_revenue_region['region']} - ${least_revenue_region['revenue']}")

# Question 2: What percentage of our returning/new customers are making a purchase when they visit the site?
# Group by visitor type and calculate the total revenue and count of visits
purchase_by_visitor_type = df.groupby('visitor_type').agg(
    total_revenue=('revenue', 'sum'),
    total_visits=('revenue', 'count')
).reset_index()

# Calculate the percentage of purchases
purchase_by_visitor_type['purchase_percentage'] = (purchase_by_visitor_type['total_revenue'] / purchase_by_visitor_type['total_visits']) * 100

# Create a bar plot for purchase percentage by visitor type
plt.figure(figsize=(8, 5))
sns.barplot(x='visitor_type', y='purchase_percentage', data=purchase_by_visitor_type)
plt.title('Purchase Percentage by Visitor Type')
plt.xlabel('Visitor Type')
plt.ylabel('Purchase Percentage (%)')
plt.show()

# Question 3: Are sales being made more on weekends comparatively to weekdays?
# Group by weekend and sum the revenue
revenue_by_weekend = df.groupby('weekend')['revenue'].sum().reset_index()

# Create a bar plot for revenue by weekend vs weekdays
plt.figure(figsize=(8, 5))
sns.barplot(x='weekend', y='revenue', data=revenue_by_weekend)
plt.title('Revenue by Weekend vs Weekday')
plt.xlabel('Weekend (1) / Weekday (0)')
plt.ylabel('Total Revenue')
plt.show()

# Question 4: Which months have been the most effective for generating sales?
# Group by month and sum the revenue
revenue_by_month = df.groupby('month')['revenue'].sum().reset_index()

# Create a bar plot for revenue by month
plt.figure(figsize=(10, 6))
sns.barplot(x='month', y='revenue', data=revenue_by_month)
plt.title('Revenue by Month')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.show()

# Question 5: Is direct/social or advertising traffic contributing heavily to sales?
# Group by traffic type and sum the revenue
revenue_by_traffic_type = df.groupby('traffic_type')['revenue'].sum().reset_index()

# Create a bar plot for revenue by traffic type
plt.figure(figsize=(10, 6))
sns.barplot(x='revenue', y='traffic_type', data=revenue_by_traffic_type)
plt.title('Revenue by Traffic Type')
plt.xlabel('Total Revenue')
plt.ylabel('Traffic Type')
plt.show()
