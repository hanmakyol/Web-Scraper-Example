import mysql.connector

# Connect to the MySQL database
db_connection = mysql.connector.connect(
    host='localhost',
    user='webscrapper',
    password='scrap1122',
    database='WebScrapperDB'
)

# Get student's input for week and grade
week = input("Enter the week number: ")
grade = input("Enter the grade (1-100): ")

# Validate grade input
try:
    grade = int(grade)
    if grade < 1 or grade > 100:
        raise ValueError("Grade must be between 1 and 100")
except ValueError:
    print("Invalid grade input. Grade must be an integer between 1 and 100.")
    db_connection.close()
    exit()

# Insert the grade into the dataset table
insert_query = f"UPDATE combined_tables SET Grade = {grade} WHERE Week = {week};"

cursor = db_connection.cursor()
cursor.execute(insert_query)
db_connection.commit()

print(f"Grade {grade} for Week {week} added successfully.")

# Close the database connection
cursor.close()
db_connection.close()