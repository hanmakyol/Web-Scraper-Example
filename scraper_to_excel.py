import requests
from bs4 import BeautifulSoup
import pandas as pd

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

df=pd.DataFrame(data, columns=None)

for i, row in enumerate(data[:5], start=1):
    print(f"Row {i}: {row}")

user_input = input("Do you want to continue?").strip().lower()

if user_input == 'y':
    df = pd.DataFrame(data, columns=None)

    df.to_excel('ELL_survey_of_english_literature.xlsx', index=False)
    
    print("Data exported successfully")

elif user_input == 'n':
    print("Canceled")