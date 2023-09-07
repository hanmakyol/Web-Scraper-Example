import mysql.connector
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

# Connect to the MySQL database
db_connection = mysql.connector.connect(
    host='localhost',
    user='webscrapper',
    password='scrap1122',
    database='WebScrapperDB'
)


# Create a cursor
cursor = db_connection.cursor()

# Execute an SQL query to retrieve data and exclude the label row
query = "SELECT Week, Grade FROM combined_tables WHERE Week != 'Week' ORDER BY CAST(Week AS SIGNED);"
cursor.execute(query)

# Fetch the data
data = cursor.fetchall()

# Separate the data into lists (e.g., weeks and grades)
weeks = [row[0] for row in data]
grades = [row[1] for row in data]

# Convert grades to a NumPy array for mathematical operations
grades = np.array(grades)  # Convert to a NumPy array

# Define a custom colormap from red (lower grades) to green (higher grades) with the range 50 to 100
cmap = LinearSegmentedColormap.from_list('red_to_green', ['#FF0000', '#00FF00'], N=51)


vmin, vmax = 50, 100  # Specify the range

# Create a bar chart with colored bars
bars = plt.bar(weeks, grades, color=cmap((grades - vmin) / (vmax - vmin)))  # Use NumPy array

# Add labels and a title
plt.xlabel('Week')
plt.ylabel('Grade')
plt.title('Student Grades by Week')

# Create a colorbar legend
sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm.set_array([])  # Adjust the colorbar's range
plt.colorbar(sm, label='Grade', pad=0.1)


# Show the plot
plt.show()

# Close the cursor and the database connection
cursor.close()
db_connection.close()