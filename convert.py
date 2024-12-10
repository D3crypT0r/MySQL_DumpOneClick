#to_conver_xlsx_file_to_csv

import pandas as pd
df = pd.read_excel('your_xlsx_dataset_file_with_absolute_path') #loading .xlsx dataset for converting purposes
df.to_csv('absolute_path_to_save_your_csv_file) #.xlsx file converted to .csv format
