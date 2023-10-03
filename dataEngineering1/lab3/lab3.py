import pandas as pd

df = pd.read_csv('data_bank.csv')

date = ['03.10.2023' for i in range(len(df))]
name = ['Foreign Currency Market' for i in range(len(df))]

df.insert(0, 'Date', date, allow_duplicates = False)
df.insert(1, 'name', name, allow_duplicates = False)

df.to_csv (r'data_bank_new.csv', index= False )

import csv
import json

data = {}

with open('data_bank_new.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')

    for row in reader:
        volute_data = {
            "Date": row['Date'],
            "name": row['name'],
            "Volute": row['Volute'],
            "ID": row['ID'],
            "NumCode": row['NumCode'],
            "Nominal": int(row['Nominal']),
            "Name": row['Name'],
        }
        data[row['Volute']] = volute_data

json_data = json.dumps(data, ensure_ascii=False, indent=2)

print(json_data)