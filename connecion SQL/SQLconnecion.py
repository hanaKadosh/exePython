import pandas as pd
import psycopg2
import os 
class Targil1:
   
    cursor = " "
    os.chdir(r'C:/log')
    """
    name=chani kadosh
    date:19-01-23
    description
    input
    output

    """
    #The func in a connacion 
    def openConnecion(self):
        server = 'CHANI-KADOSH\SQLEXPRESS'
        database = 'Exercise1'
        try:
            connection = psycopg2.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
            global cursor 
            cursor = connection.cursor()
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to Post SQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
   # get name form tha user and return id
    def returnID(self,name,fileLog):
        try:
            cursor.execute(f"SELECT id FROM Cust where name='{name}'",self.openConnecion())  
        except NameError:
           fileLog.write('The name dont exist\n')
        data = cursor.fetchall()
        for row in data:
            return row.id
    # return the order
    def returnOrder(self,cust_id,fileLog):
        try:
            cursor.execute(f"select * from Orders where customer_id={cust_id}",self.openConnecion())  
        except ValueError:
            fileLog.write('The cust not have orders\n')
        return list(cursor.fetchall())
    
    def returnSum(list):
            sum = 0
            for i in list:
                sum+=i[3]
            return sum

#  /?
    def writetoLog(fileLog,err):
        fileLog.write('No data\n')

    

    