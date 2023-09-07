import mysql.connector
import pandas as pd

# Connect to the MySQL database
db_connection = mysql.connector.connect(
    host='localhost',
    user='webscrapper',
    password='scrap1122',
    database='WebScrapperDB'
)

# Execute the modified query
query = """
    SELECT
        CAST(column1 AS SIGNED) AS Week,
        GROUP_CONCAT(column2 SEPARATOR ', ') AS Topics
    FROM (
        SELECT column1, column2 FROM classical_lit
        UNION ALL
        SELECT column1, column2 FROM survey_of_british_lit
        UNION ALL
        SELECT column1, column2 FROM textual_analysis
    ) AS combined_tables
    GROUP BY Week
    ORDER BY Week;
"""

# Fetch the results using pandas
df = pd.read_sql(query, con=db_connection)

df = df[df['Topics'] != 'Topics, Topics, Topics']

# Save the results to an Excel file
excel_file_path = "D:/ELL/datas.xlsx"
df.to_excel(excel_file_path, index=False)

# Define the target table name in the database
target_table = "combined_tables"

try:
    # Iterate through the DataFrame and insert data into the MySQL table
    for _, row in df.iterrows():
        insert_query = f"INSERT INTO {target_table} (Week, Topics) VALUES (%s, %s)"
        cursor = db_connection.cursor()
        cursor.execute(insert_query, (row['Week'], row['Topics']))
        cursor.close()

    # Commit the changes and close the database connection
    db_connection.commit()
    db_connection.close()

    print("Data imported from Excel to MySQL successfully.")

except Exception as e:
    print(f"Error: {str(e)}")

