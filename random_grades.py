import mysql.connector
import random

# Connect to the MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="datae",
    password="323414ch.",
    database="project1_data_base"
)


cursor = db_connection.cursor()

# Query to update the Grade column with random integer grades between 50 and 100
update_query = "UPDATE merged_table SET Grade = %s WHERE Week = %s;"

# Get the list of weeks in your dataset
select_weeks_query = "SELECT DISTINCT Week FROM merged_table;"
cursor.execute(select_weeks_query)
weeks = [row[0] for row in cursor.fetchall()]

# Assign random integer grades to each week
for week in weeks:
    random_grade = random.randint(50, 100)
    cursor.execute(update_query, (random_grade, week))
    db_connection.commit()
    print(f"Week {week}: Random grade {random_grade} assigned.")

# Close the cursor and the database connection
cursor.close()
db_connection.close()