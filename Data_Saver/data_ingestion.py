import sqlite3
import json
from Database.Database_Manager import *

def ingest_data(json_file):
    # Read data from JSON file
    with open(json_file, "r") as file:
        products_data = json.load(file)

    # Insert data into Products table
    insert_Data(products_data)

    # Close database connection

    print("Product details ingested into the database.")
