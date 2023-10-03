import pandas as pd

df = pd.read_csv('data_bank.csv')

date = ['03.10.2023' for i in range(len(df))]
name = ['Foreign Currency Market' for i in range(len(df))]

df.insert(0, 'Date', date, allow_duplicates = False)
df.insert(1, 'name', name, allow_duplicates = False)

df.to_csv (r'data_bank_new.csv', index= False )

