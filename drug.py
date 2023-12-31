import sqlite3
import pandas as pd

df1 = pd.read_csv('drug.csv')
conn = sqlite3.connect("db.sqlite3")

df1['chemical_structure'].fillna('Default Structure', inplace=True)
df1['Drug_ID_MESH'].fillna('Default Drug ID', inplace=True)

df1.to_sql('NaturalDrug_drug_crc', conn, if_exists='append', index=False)

conn.close()
