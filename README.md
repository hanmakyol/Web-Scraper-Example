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
