import pymysql
import pandas as pd

df = pd.read_csv('your_dataset_file_with_absolute_path')  #to load the dataset 

df = df.dropna() ## to Drop rows with NaN values

df['candidateName'] = df['candidateName'].apply(lambda x: x[:25])

conn = pymysql.connect(
    host='localhost or remote',        
    user='root',             
    password='dbpassword', 
    db='db_name'             
)

cursor = conn.cursor()

insert_query = """
INSERT INTO "yourtablename" (column1, column2, column3, column4, column5) #rename the column1 etc to your actual column names and #yourtablename to actual table name
VALUES (%s, %s, %s, %s, %s);
"""

for index, row in df.iterrows():
    cursor.execute(insert_query, (
        row['column1'],          
        row['column2'],      
        row['column3'],     
        row['column4'],    
        row['column5']
    ))

conn.commit()

print(f"Inserted {len(df)} records into 'yourtablename' table.") #rename the yourtablename to actual table name

cursor.close()
conn.close()
