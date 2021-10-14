# Importing csv and json modules
from typing import Any
import csv
import json


# Function to convert a CSV file to JSON file
# Takes the path of the files to be converted as arguments
def convert_csv_to_json(csvPath:Any, jsonPath:Any)-> Any:

            """
            I used a csv file called ratings from this link : https://github.com/gangtao/datasets/blob/master/csv/ratings.csv
            >>>convert_csv_to_json(ratings.csv,ratings.json)
            {
                    "1": {
                            "user": "1",
                            "movie": "5060",
                            "rating": "5.0",
                            "timestamp": "964984002"
                    },
                    "2": {
                            "user": "2",
                            "movie": "131724",
                            "rating": "5.0",
                            "timestamp": "1445714851"
                   },
                   ...
                   "122": {
                           "user": "122",
                           "movie": "134130",
                           "rating": "4.0",
                           "timestamp": null
                   }
            }
            Traceback (most recent call last):
            ...
            KeyError: 'wrong-key'
            """
	
	# create a empty dictionary
	data = {}
	
	# read csv file using in-built function of csv module called DictReader
	with open(csvPath, encoding='utf-8') as csvf: # don't forget to mention utf-8 encoding
		csvReader = csv.DictReader(csvf)
		
		# Convert each row into a dictionary and add it to data
		for rows in csvReader:
			
			# Assuming a column named 'id' to be the primary key
			# change the primary key name according to your csv file
			key = rows['id']
			data[key] = rows

	# Open a json writer and use the json.dumps() function to dump data
	with open(jsonPath, 'w', encoding='utf-8') as jsonf: 
		jsonf.write(json.dumps(data, indent=3)) # indent is used to improve the readability of the josn file, can be None also
		# https://docs.python.org/3/library/json.html read this documentation for difference between json.dump() and json.dumps()

# Driver Code

# Decide the two file paths according to your computer device
csvPath = r'path/to/csv/file'
jsonPath = r'path/to/json/file' # specify the path where your converted json file should be stored


# Call the convert_csv_to_json function
convert_csv_to_json(csvPath, jsonPath)
