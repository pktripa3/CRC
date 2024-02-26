import sqlite3
import pandas as pd

df1 = pd.read_csv('fda.csv')
conn = sqlite3.connect("db.sqlite3")

df1.to_sql('fda_fda_crc', conn, if_exists='append', index=False, method='multi', chunksize=1000,)

conn.close()