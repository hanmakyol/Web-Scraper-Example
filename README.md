# Web Scraping Example

In this project, I tried to understand web scraping and sql basics and wanted to upload it so people who interests can use it too. 

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Installation](#installation)
- [Usage](#usage)
- [Web Scraping](#web-scraping)
- [Importing Data to Excel](#importing-data-to-excel)
- [Assigning Grades](#assigning-grades)
- [Data Visualization](#data-visualization)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This projects aims to being an example for the ones who wants to see how a simple web scraping works and how it can be connected with a sql server. I thought of a case in which I assumed that a student should give herself a grade for the courses she took every week for a semester and what topics she should focus on in order to complete her deficiencies until the exam week.

## Prerequisites

-Python
-MySQL (or a similar database service)
-Python libraries (BeautifulSoup, Pandas, Matplotlib)


## Getting Started 

First things first, you should start with the installing necessary tools.

### Installation

For MySQL : https://www.mysql.com/downloads/ 

Choose **MySQL Installer for Windows**. 

For Python : https://www.python.org/downloads/

Choose the latest version of python.

Now we are able to use pip. 

To install the `beautifulsoup4` Python package, open your terminal and run the following command:

```shell
pip install beautifulsoup4 
```

To install the `matplotlib` Python package, open your terminal and run the following command:

```shell
pip install matplotlib 
```

To install the `mysql-connector-python` Python package, open your terminal and run the following command:

```shell
pip install mysql-connector-python 
```

To install the `pandas` Python package, open your terminal and run the following command:

```shell
pip install pandas 
```

Now we are ready to use packages and sql server.

## Usage

``` bash
mysql -u root -p
```
You will be prompted to enter the root user's password.

Lets create new user for the project.

``` sql
CREATE USER 'username'@'host' IDENTIFIED BY 'password';
```
As an example: 

``` sql
CREATE USER 'webscrapper'@'localhost' IDENTIFIED BY 'mypassword';
```
After creating the user, you may need to grant specific privileges to the user to access databases and perform actions. You can use the GRANT statement for this purpose. But before that you should create a database which we will grant permissions.

``` sql
CREATE DATABASE WebScrapperDB;
```
Now we can grant the privileges : 

``` sql
GRANT ALL PRIVILEGES ON WebScrapperDB.* TO 'webscrapper'@'localhost';
```
Finally, we are ready to go further operations. Since it is waste of time to write a code for similar actions we use scrpits. Luckily, we have installed python already. Lets write our first script. 

## Web Scrapping

Our mutual friend John is an English Language and Literature student at Ankara University. He is forgetful and wants to determine his knowledge in specific subjects in order to study accordingly, he would like to use an existing web scraper instead of manually listing all the topics for each week. For this purpose, the first step of the code we will write is to go to the university's course schedule page and perform a brief examination."


![Classical Literature](https://github.com/hanmakyol/ELL/blob/main/Introduction%20to%20classical%20literature.png)
![Selecting Element Tool](https://github.com/hanmakyol/ELL/blob/main/Getting%20Table%20Name.png)

Press **F12** and use the tool for selecting element and finding the table's name. We've found the table's name 'dersbilgileri'. In this project I also get the div which contains the our table because there is another table with the same class.

Now open your code editor create a new .py file named classical_lit_scraper.py . 

We can start coding:

1. Step Importing Packages

```python
from logging import PlaceHolder
import requests
from bs4 import BeautifulSoup
import pandas as pd
import mysql.connector
```

These are packages that we had to install to run our code. BeautifulSoup for webscrapping; mysql.connector for linking python and our mysql database; pandas for manipulating the data that we are scrapping.

2. Step Databese Connection

```python
db_connection = mysql.connector.connect(
    host='localhost',
    user='webscrapper',
    password='mypassword',
    database='WebScrapperDB'
)
```
In this step we are connecting our mysql database to our script so you can copy paste it to our future scripts and if you assigned different user name and password do not forget the change them. 

3. Step Cursor Connection

We need a cursor to execute operations in our database. 

```python
db_cursor = db_connection.cursor()
```

4. Step Web Scrapping
```python
#Using beautifulsoup for web scrapping
url = 'http://bbs.ankara.edu.tr/Ders_Bilgileri.aspx?dno=1008750&bno=1596&bot=193'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
div_element = soup.find('div', id='body_content_pnlDersAkis')

#This is the part that I mentioned, I tried to get our table specifically
if div_element: 
    target_table = div_element.find('table', class_='dersbilgileri')

#Creating a empty data list beforehand to not get errors when we try append the data from the table
data = []

if target_table:
    rows = target_table.find_all('tr')
    for row in rows:
        columns = row.find_all('td')
        row_data = [column.get_text(strip=True) for column in columns]
        data. append(row_data)
#I've decided to get rid of unnecessary parts of the data.
for row in data:
    del row[3]

#I would like to see the data here in case an error is encountered so that I can see it beforehand and not take further action.
print("Scraped Data:")
for i, row in enumerate(data, start=1):
    print(f"Row {i}: {row}")

user_input = input("Do you want to insert this data into MySQL (y/n): ").strip().lower()

if user_input == 'y':
    if data:
        column_names =[f"column{i+1}" for i in range(len(data[0]))]
        columns_string = ", ".join([f"{name} VARCHAR(255)"for name in column_names])
        #Here our cursor helps us to execute operations. Creating table
        create_table_query = f"CREATE TABLE IF NOT EXISTS classical_lit ({columns_string})" 
        db_cursor.execute(create_table_query)
        db_connection.commit()

        for row in data:
            placeholders = ", ".join(["%s"] * len(row))
            sql_insert = f"INSERT INTO classical_lit VALUES ({placeholders})"
            db_cursor.execute(sql_insert,row)
        db_connection.commit()
        print("Data inserted into MySQL successfully")

    else:
        print("No data to insert")
elif user_input == "n":
    print("Canceled")

```
and finally we are clossing our cursor and connection to database.
```python
db_cursor.close()
db_connection.close()
```
