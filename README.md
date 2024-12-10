# MySQL_DumpOneClick

#This repository provides a Python solution to convert data from an Excel (.xlsx) file into a CSV format and insert it into a MySQL database. The process includes:

# 1. Excel to CSV Conversion: Convert an Excel dataset to CSV using pandas.
Load CSV into MySQL: Insert the cleaned data (e.g., removing NaN values and truncating long strings) from the CSV file into a MySQL table using pymysql.

#Features:
a. Converts Excel files to CSV format.
b. Inserts CSV data into MySQL, handling large datasets.
c. Cleans data by removing rows with missing values and truncating specific columns.

#Requirements:
pandas and pymysql

# Usage:

#Convert Excel to CSV.
Load the CSV file into MySQL by configuring database connection details.

#Installation:

'pip install pandas pymysql or pip3 install pandas pymysql'

