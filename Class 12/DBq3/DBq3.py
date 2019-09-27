"""
Dhruv Jain
XII-D
Database Management Q3
"""

import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                   database='arcanemagic',
                                   user='root',
                                   password='amity')
cursor = connection.cursor()

a = input("Insert/Display/Search records: ").lower()

def insertIntoTable():
    itemCode = input("Enter Item Code: ")
    itemName = input("Enter Item Name: ")
    price = float(input("Enter Price: "))
    query = "INSERT INTO item values('%s', '%s', '%f');" % (itemCode, itemName, price)
    cursor.execute(query)
    connection.commit()
    
def showRecords():
    query = "SELECT * FROM item;"
    cursor.execute(query)
    for i in cursor.fetchall():
        print(i)

def searchRecords():
    itemCode = input("Enter Item Code: ")
    query = "SELECT * FROM item WHERE Itemcode = '%s';" % (itemCode)
    cursor.execute(query)
    for i in cursor.fetchall():
        print(i)

if a == "insert":
    insertIntoTable()
elif a == "display":
    showRecords()
elif a == "search":
    searchRecords()
else:
    print("Unknown operation")