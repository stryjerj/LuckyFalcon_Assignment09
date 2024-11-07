#main.py

# Name: Roman Stryjewski, Cheikh Abdoul
# email:  stryjerj@mail.uc.edu, abdoulch@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 11/07/2024
# Course #/Section:  IS4010 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  Accessing a database and using queries to produce a product that states information about the database

# Brief Description of what this module does: The main module where the queries are written to achieve the final product, as well as sotring it in variables
# Citations:
# Anything else that's relevant:

import pyodbc
import random
from utilitiesPackage.utilities import *

if __name__ == "__main__":
    try: 
        conn = connect_to_database()

        cursor = conn.cursor()
    
    except Exception as e:
        print("Error Accessing DB")
        print(e)
        exit()


    # 1.
    cursor.execute( 'SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct' )
    products = cursor.fetchall()

    # 2.
    random_product = random.choice(products)

    #Storing the variables of the random product
    product_id = random_product.ProductID
    description = random_product.Description
    manufacturer_id = random_product.ManufacturerID
    brand_id = random_product.BrandID

    # 3.
    cursor.execute(" SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = ?", manufacturer_id)

    # 4. Storing the manufacturer name into a variable
    manufacturer = cursor.fetchone()[0]

    # 5.
    cursor.execute("SELECT Brand FROM tBrand WHERE BrandID = ?", brand_id)

    # Storing the Brand name in a variable
    brand = cursor.fetchone()[0]

    # 6.
    cursor.execute("""
        SELECT TOP (100) PERCENT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold
        FROM dbo.tTransactionDetail
        INNER JOIN dbo.tTransaction ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID
        WHERE (dbo.tTransaction.TransactionTypeID = 1) AND (dbo.tTransactionDetail.ProductID = ?)
    """, product_id)

    # Storing the Number of Items Sold in a variable
    number_of_items_sold = cursor.fetchone()[0]

    # 7.
    finalProduct = f"{manufacturer}, the manufacturer of the brand {brand}, produces the product '{description}', which has sold {number_of_items_sold} units."
    print(finalProduct)


    cursor.close()
    conn.close()

