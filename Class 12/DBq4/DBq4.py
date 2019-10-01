"""
Dhruv Jain
XII-D
Database Management Q4
"""

import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                   database='arcanemagic',
                                   user='root',
                                   password='amity')
cursor = connection.cursor()

a = None

def insertIntoTable():
    roll = int(input("Roll no: "))
    name = input("Name: ")
    grade = int(input("Class: "))
    dob = int(input("Date of birth: "))
    gender = input("Gender: ")    
    query = "INSERT INTO student values('%d', '%s', '%d', '%d', '%s');" % (roll, name, grade, dob, gender)
    cursor.execute(query)
    connection.commit()

def updateRecords():
    roll = int(input("Roll no to update: "))
    name = input("Updated name: ")
    grade = int(input("Updated class: "))
    dob = int(input("Updated date of birth: "))
    gender = input("Updated gender: ")
    query = "UPDATE student set Name='%s',Class='%d',DOB='%d',Gender='%s' where RollNo='%d';" % (name, grade, dob, gender, roll)
    cursor.execute(query)
    connection.commit()

while a != "exit":
    a = input("Insert record/Update record/Exit: ").lower()
    if a == "insert":
        insertIntoTable()
    elif a == "update":
        updateRecords()