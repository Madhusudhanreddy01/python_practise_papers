# 14.Define a function which can read json file and displays the data present in it to the 
# console in dictionary format
# Note : Please create .json file and store the sample data in it and read the json file, 
# display the data in dictionary format


import json

def open_json():
    with open("_14_data.json") as f:
        data=json.load(f)
    print(data)

open_json()