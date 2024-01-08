import sqlite3
import pandas as pd

df1 = pd.read_csv('metabolite.csv')
conn = sqlite3.connect("db.sqlite3")

df1.to_sql('metabolo_metabolo_crc', conn, if_exists='append', index=False, method='multi', chunksize=1000,)

conn.close()