# Question 1: The count of the operating systems used to visit the site and the percentage of the total

import pandas as pd

# Load the dataset
df = pd.read_csv('cleaned_data_no_bounce_rate.csv')

# Count occurrences of each operating system
os_counts = df['operating_systems'].value_counts()

# Convert to percentage
os_percentage = (os_counts / os_counts.sum()) * 100

# Print results
print("Operating System Count:\n", os_counts)
print("\nOperating System Percentage:\n", os_percentage)

# Question 2: The amount of users visiting the site using mobile operating system and desktop operating systems
# Categorising operating systems into Mobile and Desktop
mobile_os = ['Android', 'iOS']
desktop_os = ['Windows', 'MACOS', 'ChromeOS', 'Ubuntu', 'Other']

# Creating a new column to classify devices
df['device_type'] = df['operating_systems'].apply(lambda x: 'Mobile' if x in mobile_os else 'Desktop')

# Counting users by device type
device_counts = df['device_type'].value_counts()
device_percentage = df['device_type'].value_counts(normalize=True) * 100

# Output results
print("Device Type Count:\n", device_counts)
print("\nDevice Type Percentage:\n", device_percentage)

#Question 3: The most commonly used browsers and their breakdown on mobile versus desktop
import pandas as pd

# Load the cleaned data
df = pd.read_csv("cleaned_data_no_bounce_rate.csv")

# Group by 'browser' and 'operating_systems' (mobile or desktop)
browser_device_breakdown = df.groupby(['browser', 'operating_systems']).size().unstack(fill_value=0)

# Display the breakdown
print(browser_device_breakdown)

#Question 4: 
import pandas as pd

# Load the dataset
df = pd.read_csv("cleaned_data_no_bounce_rate.csv")

# Create a cross-tabulation of operating systems by region
os_by_region = df.groupby(['region', 'operating_systems']).size().unstack(fill_value=0)

# Display the result
print(os_by_region)



