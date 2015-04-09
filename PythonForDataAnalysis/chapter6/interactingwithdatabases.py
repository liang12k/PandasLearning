"""
SQL-based relation databases
-SQL server ie: PostgreSQL, MySQL
-non-SQL server ie: NoSQL

database choice dependent on application's:
-performance
-data integrity
-scalability
"""

import sqlite3
import pandas as pd

query="""
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20), c REAL, d INTEGER);
"""
con=sqlite3.connect(":memory:")
# print con # <sqlite3.Connection at 0x1046823d0>
con.execute(query)
con.commit()

data=[
    ("Atlanta","Georgia",1.25,6),
    ("Tallahassee","Florida",2.6,3),
    ("Sacramento","California",1.7,5)
]
stmt="INSERT INTO test VALUES(?,?,?,?)"
con.executemany(stmt,data)
con.commit()

cursor=con.execute("SELECT * FROM test")
rows=cursor.fetchall()
print rows
"""
[(u'Atlanta', u'Georgia', 1.25, 6), (u'Tallahassee', u'Florida', 2.6, 3), (u'Sacramento', u'California', 1.7, 5)]
"""
