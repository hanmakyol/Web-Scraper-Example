from logging import PlaceHolder
import requests
from bs4 import BeautifulSoup
import pandas as pd
import mysql.connector

db_connection = mysql.connector.connect(
    host='localhost',
    user='datae',
    password='323414ch.',
    database='project1_data_base'
)

db_cursor = db_connection.cursor()



url = 'http://bbs.ankara.edu.tr/Ders_Bilgileri.aspx?dno=1008749&bno=1596&bot=193'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

div_element = soup.find('div', id='body_content_pnlDersAkis')


if div_element: 
    target_table = div_element.find('table', class_='dersbilgileri')

data = []

if target_table:
    rows = target_table.find_all('tr')
    for row in rows:
        columns = row.find_all('td')
        row_data = [column.get_text(strip=True) for column in columns]
        data. append(row_data)

for row in data:
    del row[3]

print("Scraped Data:")
for i, row in enumerate(data, start=1):
    print(f"Row {i}: {row}")

user_input = input("Do you want to insert this data into MySQL (y/n): ").strip().lower()

if user_input == 'y':
    if data:
        column_names =[f"column{i+1}" for i in range(len(data[0]))]
        columns_string = ", ".join([f"{name} VARCHAR(255)"for name in column_names])

        create_table_query = f"CREATE TABLE IF NOT EXISTS project1_data_table ({columns_string})"
        db_cursor.execute(create_table_query)
        db_connection.commit()

        for row in data:
            placeholders = ", ".join(["%s"] * len(row))
            sql_insert = f"INSERT INTO project1_data_table VALUES ({placeholders})"
            db_cursor.execute(sql_insert,row)
        db_connection.commit()
        print("Data inserted into MySQL successfully")

    else:
        print("No data to insert")
elif user_input == "n":
    print("Canceled")

db_cursor.close()
db_connection.close()
