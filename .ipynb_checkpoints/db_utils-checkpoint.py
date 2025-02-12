import yaml
import pandas as pd
from sqlalchemy import create_engine

class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.credentials = credentials
        print("initialized with credentials.")

    def initialize_engine(self):
        user = self.credentials['RDS_USER']
        password = self.credentials['RDS_PASSWORD']
        host = self.credentials['RDS_HOST']
        database = self.credentials['RDS_DATABASE']
        port = self.credentials['RDS_PORT']
        
        connection_string = f'postgresql://{user}:{password}@{host}:{port}/{database}'
        engine = create_engine(connection_string)
        print("SQLAlchemy engine initialized.")
        return engine

    def extract_data(self, table_name):
        engine = self.initialize_engine()  
        query = f"SELECT * FROM {table_name}" 
        df = pd.read_sql(query, engine) 
        print(f"Data extracted from {table_name}.")
        return df

    def save_to_csv(self, df, filename="customer_activity.csv"):
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}.")

def load_db_credentials(filepath="credentials.yaml"):
    with open(filepath, "r") as file:
        return yaml.safe_load(file)

if __name__ == "__main__":
    creds = load_db_credentials()
    db_connector = RDSDatabaseConnector(creds)
    df = db_connector.extract_data("customer_activity")
    db_connector.save_to_csv(df)


#Task 3: load the data from my local machine into a pandas DataFrame

import pandas as pd

def load_local_data(filename="customer_activity.csv"):
    df = pd.read_csv(filename)
    print(f"Data Shape: {df.shape}") 
    print(df.head())
    return df 
df = load_local_data()

