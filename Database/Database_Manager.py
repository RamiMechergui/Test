import sqlite3 
import os 

def Connect():
    database_file = 'pascalcoste-shopping.db'

    # Check if the database file exists
    if not os.path.exists(database_file):
        Connect__To_Database = sqlite3.connect(database_file)
        DB_Cursor = Connect__To_Database.cursor()

        DB_Cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        price TEXT,
                        brand TEXT,
                        imageUrl TEXT,
                        productUrl TEXT
                      )''')

        # Commit changes and close connection
        Connect__To_Database.commit()
        Connect__To_Database.close()
        print("Database created successfully")

def insert_Data(Products_Data): 
    Connect()
    conn = sqlite3.connect('pascalcoste-shopping.db')
    cursor = conn.cursor()

    insert_data = [(product['product_name'], product['product__price'], product['product_brand'], product['image_url'], product['product_url']) for product in Products_Data]

# Insert data into Products table
    cursor.executemany('''INSERT INTO Products (name, price, brand, imageUrl, productUrl)
                      VALUES (?, ?, ?, ?, ?)''', insert_data)

# Commit changes and close connection
    conn.commit()
    conn.close()
