import csv
import json
from datetime import datetime

current_date = datetime.now().strftime("%d.%m.%Y")
data = {"Date": current_date, "name": "Company"}
valute_data = {}

with (open('data_bank.csv', newline='', encoding='utf-8') as csvfile):
    reader = csv.DictReader(csvfile, delimiter=',')

    for row in reader:
        valute_data[row["Valute"]] ={
             "ID": row['ID'],
             "NumCode": row['NumCode'],
             "CharCode": row['CharCode'],
             "Nominal": int(row['Nominal']),
             "Name": row['Name'],
             "Value": row['Value']
        }

data["Valute"] = valute_data

with open('output.json', 'w') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
