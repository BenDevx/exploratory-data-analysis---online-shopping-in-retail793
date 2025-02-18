import pandas as pd

def load_data(file_path):
    """Loads the dataset from the CSV file."""
    return pd.read_csv(file_path)

def question_1(df):
    """Q1: Are sales proportionally happening more on weekends?"""
    print(df.info())
    print(df.head())

def question_2(df):
    """Q2: Which regions are generating the most revenue currently?"""
    revenue_by_region = df.groupby('region')['revenue'].sum().sort_values(ascending=False)
    print("Revenue by Region:\n", revenue_by_region)

def question_3(df):
    """Q3: Is there any particular website traffic that stands out when generating sales?"""
    traffic_sales = df.groupby('traffic_type')['revenue'].sum().sort_values(ascending=False)
    print("Traffic Sales Breakdown:\n", traffic_sales)

def question_4(df):
    """Q4: What percentage of time is spent on the website performing administrative/product or informational related tasks?"""
    admin_time = df['administrative_duration'].sum()
    info_time = df['informational_duration'].sum()
    product_time = df['product_related_duration'].sum()
    total_time = admin_time + info_time + product_time
    
    print("Total time spent on each task:")
    print(f"Administrative Tasks: {admin_time}")
    print(f"Informational Tasks: {info_time}")
    print(f"Product-related Tasks: {product_time}")
    
    return total_time, admin_time, info_time, product_time

def question_5(admin_time, info_time):
    """Q5: Are there any informational/administrative tasks which users spend time doing most?"""
    if admin_time > info_time:
        print("Users spend more time on Administrative tasks.")
    else:
        print("Users spend more time on Informational tasks.")

def question_6(df):
    """Q6: What is the breakdown of months making the most sales?"""
    sales_by_month = df.groupby('month')['revenue'].sum().sort_values(ascending=False)
    print("Sales by Month:\n", sales_by_month)

def main():
    """Main function to run all analysis."""
    df = load_data('cleaned_data_no_bounce_rate.csv')
    question_1(df)
    question_2(df)
    question_3(df)
    total_time, admin_time, info_time, product_time = question_4(df)
    question_5(admin_time, info_time)
    question_6(df)

if __name__ == "__main__":
    main()
