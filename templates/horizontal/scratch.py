from operator import itemgetter
import sqlite3 as db
import json
from rich import print

# Sqlite experiments

dbname = "test.db"

con = db.connect(dbname)

cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")

cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")





confighistorytable_create = """
CREATE TABLE IF NOT EXISTS confighistory(year, month, day, hour, minute, second, configdata)
"""

cur.execute(confighistorytable_create)


val = {
    "hello":"yello"
}

cur.execute("INSERT INTO confighistory VALUES(?,?,?,?,?,?,?)",(2025,5,23,10,33,3,json.dumps(val)))

cur.execute("SELECT (year,configdata) FROM confighistory")
results = cur.fetchall()

for r in results:
    print(r)

con.commit()

