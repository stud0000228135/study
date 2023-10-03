import csv
import json
from datetime import datetime

date = datetime.now().date()
def make_json():
    data = {}

    # Open a csv reader called DictReader
    with open('data_bank.csv', encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            key = rows['Valute']
            data[key] = rows

    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open('output.json', 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


make_json()