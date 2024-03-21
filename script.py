from Scrapper.Data_Scraper import *
from Database.Database_Manager import *
from Data_Saver.data_saver import * 
from Data_Saver.data_ingestion import * 

Connect()
Targeted_Website = 'https://www.pascalcoste-shopping.com/esthetique/fond-de-teint.html'
Json_File_Path = './product__List.json'    
    
#Scrap Products data 
Products_Data = Data_Scraping(Targeted_Website)

#Save products data to json file
save_to_json(Products_Data)

#Insert Data
insert_Data(Products_Data)

# Ingest the extracted product data (from the JSON file) into the designed database schema.
ingest_data(Json_File_Path)


