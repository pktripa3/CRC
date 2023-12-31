import sqlite3
import pandas as pd

df1 = pd.read_csv('metabolite.csv')
conn = sqlite3.connect("db.sqlite3")

df1['Citation'] = df1['Citation'].fillna('Default Citation')
df1 = df1.dropna(subset=['Citation'])
df1.to_sql('metabol_metabolite_crc', conn, if_exists='append', index=False, method='multi', chunksize=1000,
           dtype={'Citation': 'TEXT DEFAULT "Default Citation"'})

conn.close()