import sqlite3
import time
import datetime 

#conn = sqlite3.connect('databasesql')
#cursor = conn.cursor()

date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime("%Y-%m-%d %H:%M:%S"))

file = open("datevalue.txt","w") 
file.write(date) 
file.close()

# sql = 'SELECT * FROM pointvalues WHERE ID = ?'

def creat_table():
     cursor.execute("CREATE TABLE IF NOT EXISTS POINTVALUES (ID integer, valor real, timestamp1 blob)")


def inserir(ID, valor=0):
    #cursor.execute("INSERT INTO pointvalues VALUES (111, '2021-05-3')")
    date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime("%Y-%m-%d %H:%M:%S"))
    cursor.execute('INSERT INTO pointvalues (ID, valor, timestamp1) VALUES (?, ?,?)',(ID, valor, date))
    conn.commit()


def lerTudo():
    cursor.execute("SELECT * FROM pointvalues")
    print(cursor.fetchall())


# msa_drivers = [x for x in pyodbc.drivers()]
# print(f'MS-Access Drivers: {msa_drivers}')

