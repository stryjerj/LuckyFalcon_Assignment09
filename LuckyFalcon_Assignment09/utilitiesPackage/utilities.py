# *****************************************************
# Name: Cheikh Abdoul, Roman Stryjewski
# email:  abdoulch@mail.uc.edu, stryjerj@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:   11/07/2024 
# Course #/Section:   IS 4010 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment: Accessing the Grocery Store Simulator database
# Brief Citations: N/A
# Anything else that's relevant:
# *****************************************************

#utilities.py

import pyodbc

def connect_to_database():
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
        'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
        'Database=GroceryStoreSimulator;'
        'uid=IS4010Login;'
        'pwd=P@ssword2;')

        cursor = conn.cursor()

    except:
        conn = None

    return conn 
