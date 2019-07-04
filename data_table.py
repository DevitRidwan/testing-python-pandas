import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

# get connected to the database
connection = pg.connect("host=localhost dbname=test_female user=postgres password=devitx2y")
 
dataframe = psql.read_sql_query("select id "+'"ID"'+", concat(firstname,lastname) "+'"Full Name"'+", email "+'"Email"'+", item "+'"Item"'+", quantity "+'"Quantity"'+", total_price "+'"Total Price"'+" from customer;", connection)

ahha = pd.pivot_table(dataframe, index='Full Name', columns='Item', values='Quantity')