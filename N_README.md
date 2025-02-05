## Project Title
Retail Data Project

## Project Description
This project is to extract online shopping data from an AWS RDS database. It involves creating methods to extract data, saves it locally then load it into a Pandas DataFrame.

## What I Learned:
- I learned how to connect to the AWS RDS using Python.
- Then using SQLAlchemy and Pandas to interact with databases.
- I also learnt how to handle credentials securely with `credentials.yaml`.

## Installation Instructions
1. Clone the repository to your computer.
2. Install the necessary Python libraries by running a simple command
3. Make sure you have the required credentials for connecting to the database.

## Usage Instructions
1. Open the project folder on your computer.
2. Run the Python script to extract the data from the database.
3. The data will be saved as a CSV file, and a preview of the data will be shown on the screen.


## File Structure
- **db_utils.py**: The main script where the code runs.
- **credentials.yaml**: File with your database login details (kept secret).
- **requirements.txt**: A list of libraries needed to run the project.
- **README.md**: This file with project details.
- **.gitignore**: List of files to be ignored by Git (like credentials.yaml).

## License information
