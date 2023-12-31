import sqlite3
import pandas as pd

df1 = pd.read_csv('family.csv')

df1 = df1.loc[:, ~df1.columns.str.contains('^Unnamed')]
conn = sqlite3.connect("db.sqlite3")

df1['Plant_common_name'].fillna('Default Plant Common Name', inplace=True)
df1['Scientific_Name'].fillna('Default Scientific Name', inplace=True)
df1['Family'].fillna('Default Family', inplace=True)

df1.to_sql('fam_fam_crc', conn, if_exists='append', index=False)

conn.close()

