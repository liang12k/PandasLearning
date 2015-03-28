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
# # since there are only 3 headers ('a','b','c')
# # col index 3 is omitted (missing '4' value)
datadict
# {'a': ('1', '1'), 'b': ('2', '2'), 'c': ('3', '3')}
pd.DataFrame(datadict)
'''
   a  b  c
0  1  2  3
1  1  2  3
'''

# # note: have to add quoting attribute
# # see : http://www.oreilly.com/catalog/errata.csp?isbn=0636920023784
class mydialect(csv.Dialect):
    lineterminator="\n"
    delimiter=";"
    quotechar='"'
    quoting=csv.QUOTE_MINIMAL

reader=csv.reader(f,dialect=mydialect)
# <_csv.reader at 0x1136e59f0>

reader=csv.reader(f,delimiter="|")
# <_csv.reader at 0x1136ccc90>

# # manually write delimited files
with open("samplemanual_writedata.csv","w") as f:
    writer=csv.writer(f,dialect=mydialect)
    writer.writerow(("one","two","three"))
    writer.writerow(list("123"))
    writer.writerow(list("456"))
    writer.writerow(list("789"))
sampledata_reader=csv.reader(
    open("samplemanual_writedata.csv"),
    delimiter=";"
)
print list(sampledata_reader)
# [['one', 'two', 'three'], ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]


# # Table 6-3: CSV dialect options
{'delimiter': "One-character string to separate fields. Defaults to ','.",
 'doublequote': 'How to handle quoting character inside a field. If True, it is doubled. See online documentation for full detail and behavior.',
 'escapechar': 'String to escape the delimiter if quoting is set to csv.QUOTE_NONE. Disabled by default',
 'lineterminator': "Line terminator for writing, defaults to '\r\n'. Reader ignores this and recognizes cross platform line terminators.",
 'quotechar': 'Quote character for fields with special characters (like a delimiter). Default is \'"\'.',
 'quoting': "Quoting convention. Options include csv.QUOTE_ALL (quote all fields), csv.QUOTE_MINIMAL (only fields with special characters like the delimiter), csv.QUOTE_NONNUMERIC, and csv.QUOTE_NON (no quoting). See Python's documentation for full details. Defaults to QUOTE_MINIMAL.",
 'skipinitialspace': 'Ignore whitespace after each delimiter. Default False.'}
