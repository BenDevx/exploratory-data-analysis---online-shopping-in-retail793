# Retail Data Analysis Project

## Table of Contents
1. Project Description
2. Installation Instructions
3. Usage Instructions
4. File Structure
5. License Information

---

## Project Description
This project involves extracting and analyzing online shopping data from an AWS RDS database. The goal is to clean, transform, and analyze the dataset to ensure accuracy, consistency, and better insights.

### **Key Steps in the Project:**
- **Data Extraction:** Connecting to AWS RDS using Python and extracting relevant retail data.
- **Data Storage:** Saving extracted data locally for further processing.
- **Data Cleaning & Transformation:**
  - **Correcting Column Formats:** Ensuring numerical and categorical values are in the correct format.
  - **Handling Missing Values:** Identifying and imputing or removing missing values where necessary.
  - **Transforming Skewed Columns:** Addressing skewed numerical distributions for better statistical analysis.
  - **Detecting and Removing Outliers:** Identifying and eliminating outliers to enhance data quality.
  - **Removing Highly Correlated Columns:** Eliminating highly correlated features to prevent multicollinearity.

These transformations ensure the dataset is well-prepared for further analysis and modeling.



---

## Usage Instructions
### **Data Extraction:**
1. Open the project folder on your computer.
2. Run the Python script to extract data from the AWS RDS database:
   ```sh
   python db_utils.py
   ```
3. The extracted data will be saved as a CSV file for further processing.


Each script includes visualization steps to assess the impact of the transformations.


---

### **What I Learned:**
- Connecting to AWS RDS using Python.
- Using SQLAlchemy and Pandas to interact with databases.
- Handling credentials securely with `credentials.yaml`.
- Applying key data cleaning and transformation techniques for EDA.

