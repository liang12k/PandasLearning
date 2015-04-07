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

