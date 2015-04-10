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

query="SELECT * FROM test"
cursor=con.execute(query)
rows=cursor.fetchall()
print rows
'''
[(u'Atlanta', u'Georgia', 1.25, 6), (u'Tallahassee', u'Florida', 2.6, 3), (u'Sacramento', u'California', 1.7, 5)]
'''
print cursor.description
# note the col names in index 0 of tuples
'''
(('a', None, None, None, None, None, None), ('b', None, None, None, None, None, None), ('c', None, None, None, None, None, None), ('d', None, None, None, None, None, None))
'''
print zip(*cursor.description)
# * is a splat operator
# http://stackoverflow.com/questions/5917522/unzipping-and-the-operator
# feed each elem of *elems as an arg to zip()
'''
[('a', 'b', 'c', 'd'),
 (None, None, None, None),
 (None, None, None, None),
 (None, None, None, None),
 (None, None, None, None),
 (None, None, None, None),
 (None, None, None, None)]
'''
print pd.DataFrame(
    rows,
    # * passes in cursor.desciption as list of tuples
    columns=zip(*cursor.description)[0]
)
'''
             a           b     c  d
0      Atlanta     Georgia  1.25  6
1  Tallahassee     Florida  2.60  3
2   Sacramento  California  1.70  5
'''
print pd.io.sql.read_sql(query,con)
# note: .read_frame is deprecated
'''
             a           b     c  d
0      Atlanta     Georgia  1.25  6
1  Tallahassee     Florida  2.60  3
2   Sacramento  California  1.70  5
'''
