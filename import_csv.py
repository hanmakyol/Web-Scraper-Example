import mysql.connector
import csv

db_connection = mysql.connector.connect(
    host='localhost',
    user='datae',
    password='323414ch.',
    database='project1_data_base'
)

query = "SELECT * FROM merged_table"
cursor = db_connection.cursor()
cursor.execute(query)

results = cursor.fetchall()

csv_file_path = "D:/ELL/merged_table.csv"

with open(csv_file_path, "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description])  # Write column headers
    csv_writer.writerows(results)  # Write data rows

cursor.close()
db_connection.close()

print("CSV file created successfully.")