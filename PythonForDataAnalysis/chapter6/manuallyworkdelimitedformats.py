"""
pandas.read_table
-load tabular data from disk, generally

csv.reader
-built in Python module
-handles files with single character delimiter
"""

import csv
import pandas as pd

list(open("ex7.csv"))
# ['"a","b","c"\n', '"1","2","3"\n', '"1","2","3","4"\n']
f=open("ex7.csv")
reader=csv.reader(f)
for line in reader:
    print line
'''
['a', 'b', 'c']
['1', '2', '3']
['1', '2', '3', '4']
'''
# wrangling needed, missing a col for row index 1
lines=list(csv.reader(open("ex7.csv")))
header,values = lines[0],lines[1:]
datadict={h:v for h,v in zip(header,zip(*values))}
# # note: zip(*values) applies zip onto values itself
# [('1', '1'), ('2', '2'), ('3', '3')]
datadict
# {'a': ('1', '1'), 'b': ('2', '2'), 'c': ('3', '3')}
