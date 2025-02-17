# Exploratory Data Analysis - Online Shopping in Retail

## Table of Contents
1. Project Description
2. Installation Instructions
3. Usage Instructions
4. File Structure
5. License Information

## Project Description
This project involves performing Exploratory Data Analysis (EDA) on a dataset related to online shopping in the retail industry. The goal is to clean and transform the data to ensure accuracy, consistency, and better insights. The following transformations have been applied:

- **Correcting Column Formats**: Ensured numerical and categorical values were in the correct format.
- **Handling Missing Values**: Identified and imputed or removed missing values where necessary.
- **Transforming Skewed Columns**: Addressed skewed numerical distributions to improve statistical analysis.
- **Detecting and Removing Outliers**: Identified outliers and removed them to enhance data quality.
- **Removing Highly Correlated Columns**: Eliminated highly correlated columns to prevent multicollinearity.

These transformations ensure the dataset is well-prepared for further analysis and modelling.

## Installation Instructions
To run this project, I ensured I had the following installed:

- Python3
- Pandas
- NumPy
- Matplotlib
- Seaborn


## Usage Instructions
1. Load the dataset from `cleaned_data.csv`.
2. Run the transformation scripts in order:
   - Column formatting corrections
   - Handling missing values
   - Skewed data transformation
   - Outlier detection and removal
   - Highly correlated column removal
3. The final cleaned dataset is saved as `cleaned_data_no_bounce_rate.csv`.

Each script includes visualisation steps to assess the impact of the transformations.

## File Structure
```
├── cleaned_data.csv  # Initial cleaned dataset
├── cleaned_data_no_bounce_rate.csv  # Final transformed dataset
├── transform_columns.py  # Script for correcting column formats
├── handle_missing_values.py  # Script for handling missing values
├── transform_skewed_columns.py  # Script for handling skewed distributions
├── remove_outliers.py  # Script for detecting and removing outliers
├── remove_highly_correlated_columns.py  # Script for handling correlated columns
└── README.md  # Project documentation
```


