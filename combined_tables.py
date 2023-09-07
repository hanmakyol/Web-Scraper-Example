import mysql.connector
import pandas as pd

# Connect to the MySQL database
db_connection = mysql.connector.connect(
    host='localhost',
    user='webscrapper',
    password='scrap1122',
    database='WebScrapperDB'
)

# Create the combined_tables table
create_table_query = """
    CREATE TABLE IF NOT EXISTS combined_tables (
        Week INT,
        Topics VARCHAR(255)
    )
"""
cursor = db_connection.cursor()
cursor.execute(create_table_query)

# Commit the table creation
db_connection.commit()

# Execute the modified query to populate the combined_tables table
query = """
    INSERT INTO combined_tables (Week, Topics)
    SELECT
        CAST(column1 AS SIGNED) AS Week,
        GROUP_CONCAT(column2 SEPARATOR ', ') AS Topics
    FROM (
        SELECT column1, column2 FROM classical_lit
        UNION ALL
        SELECT column1, column2 FROM survey_of_british_lit
        UNION ALL
        SELECT column1, column2 FROM textual_analysis
        WHERE column1 REGEXP '^[0-9]+$'  -- Filter out non-integer 'Week' values
    ) AS merged_data
    GROUP BY Week
    ORDER BY Week;
"""

cursor.execute(query)

# Commit the data insertion
db_connection.commit()

# Close the database connection
cursor.close()
db_connection.close()

print("Table 'combined_tables' created and populated successfully.")
