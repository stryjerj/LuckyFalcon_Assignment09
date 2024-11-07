# *****************************************************
# Name: Cheikh Abdoul
# email:  abdoulch@mail.uc.edu
# Assignment Number: Assignment06
# Due Date:   11/06/2024 
# Course #/Section:   001
# Semester/Year:   fall 2024
# Brief Description of the assignment: Accessing data from the Grocery Store Simulator database, and produces results.
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
