import mysql.connector

# Connect to the MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="datae",
    password="323414ch.",
    database="project1_data_base"
)

# Get student's input for week and grade
week_input = input("Enter the week number: ")
grade_input = input("Enter the grade (1-100): ")

# Validate grade input
try:
    grade = int(grade_input)
    if grade < 1 or grade > 100:
        raise ValueError("Grade must be between 1 and 100")
except ValueError:
    print("Invalid grade input. Grade must be an integer between 1 and 100.")
    db_connection.close()
    exit()

# Search for the week value in the dataset based on the input
search_query = f"SELECT Week FROM merged_table WHERE Week LIKE '%{week_input}%';"


cursor = db_connection.cursor()
cursor.execute(search_query)
result = cursor.fetchone()

if result:
    week = result[0]
    # Update the grade for the found week
    update_query = f"UPDATE merged_table SET Grade = {grade} WHERE Week = '{week}';"
    cursor.execute(update_query)
    db_connection.commit()
    print(f"Grade {grade} for Week {week} added successfully.")
else:
    print(f"Week {week_input} not found in the dataset.")

# Close the database connection
cursor.close()
db_connection.close()