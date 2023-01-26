import pyodbc
import pandas as pd
import psycopg2


server = 'CHANI-KADOSH\SQLEXPRESS'
database = 'Exercise1'
try:
    connection = psycopg2.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM order")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

# server = 'CHANI-KADOSH\SQLEXPRESS'
# database = 'Exercise1'

# cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
# cursor = cnxn.cursor()
# cursor.execute("SELECT * FROM order")
# def retrnOrder():
#     name=input("enret you name")
#     cursor.execute("SELECT * FROM order")

if __name__ == '__main':
    print('main')
    server = 'CHANI-KADOSH\SQLEXPRESS'
    database = 'Exercise1'
    try:
        connection = psycopg2.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM order")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

