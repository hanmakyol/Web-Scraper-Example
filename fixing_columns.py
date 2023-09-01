import mysql.connector
import pandas as pd

# Connect to the MySQL database
db_connection = mysql.connector.connect(
    host='localhost',
    user='datae',
    password='323414ch.',
    database='project1_data_base'
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

# Close the database connection
db_connection.close()

print("Results exported to Excel successfully.")