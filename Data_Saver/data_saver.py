import json

def save_to_json(Products_Data):
    Output_File = "product__List.json"

    with open(Output_File, "w") as json_file:
      json.dump(Products_Data, json_file, indent=4)

    print("Product details saved to:", Output_File)