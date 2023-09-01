import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="datae",
    password="323414ch.",
    database="project1_data_base"
)

db_cursor = db_connection.cursor()

sql_query = "SELECT * FROM classical_lit"
db_cursor.execute(sql_query)

rows = db_cursor.fetchall()

for row in rows:
    print(row)

    db_cursor.close()
    db_connection.close()