import pandas as pd
import sqlite3

# load CSV into pandas
df = pd.read_csv("resale-flat-prices.csv")

# connect and write to SQLite
conn = sqlite3.connect("hdb.db")
df.to_sql("resale", conn, if_exists="replace", index=False)

# query for the average resale price for each town and year
query = """
SELECT
    town,
    substr(month, 1, 4) AS year,
    AVG(resale_price) AS average_price
FROM resale
GROUP BY town, year
ORDER BY town, year
"""

result = pd.read_sql(query, conn)
print(result.head(20))

conn.close()