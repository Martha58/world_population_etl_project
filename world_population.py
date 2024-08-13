import pandas as pd
import sqlite3

#read the dataset
df = pd.read_csv('world_population.csv')

#data transformation
df.duplicated()
df.drop_duplicates(inplace=True)

#load into the database
conn = sqlite3.connect('world_population_sqlite3.db')

table_name = 'world_population'

df.to_sql(table_name, conn, if_exists='replace')

conn.close()