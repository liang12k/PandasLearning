"""
convert text datat into a DataFrame
"""

# # table 6-1: pandas parsing functions
{'read_clipboard': 'Version of read_table that reads data from the clipboard. Useful for converting tables from web pages',
 'read_csv': 'Load delimited data from a file, URL, or file-like object. Use comma as default delimiter',
 'read_fwf': 'Read data in fixed-width column format (that is, no delimiters)',
 'read_table': "Load delimited data from a file, URL, or file-like object. Use tab ('\t') as default delimiter"}

'''
Indexing: 
treat 1+ cols as the returned DataFrame
col names from file, user, or not at all

Type inference, data conversion:
user-defined value conversions and 
custom list of missing value markers

Datetime parsing: 
combining capability - date,time information
spread over multiple cols into single col in result

Iterating:
iterating support over chunks of very large files

Unclean data issues:
skipping content (rows, footer, comments, etc)
'''

import pandas as pd

# # Type inference
# # no need to specify col types
df=pd.read_csv("ex1.csv")
df
'''
   a   b   c   d message
0  1   2   3   4   hello
1  5   6   7   8   world
2  9  10  11  12     foo
'''
pd.read_csv("ex2.csv")
'''
   1   2   3   4  hello
0  5   6   7   8  world
1  9  10  11  12    foo
'''
pd.read_csv("ex2.csv",header=None)
# default numerical header names
'''
   0   1   2   3      4
0  1   2   3   4  hello
1  5   6   7   8  world
2  9  10  11  12    foo
'''
pd.read_csv(
    "ex2.csv",
    names=["a","b","c","d","message"]
)
# assigning col names
'''
   a   b   c   d message
0  1   2   3   4   hello
1  5   6   7   8   world
2  9  10  11  12     foo
'''
names=["a","b","c","d","message"]
pd.read_csv(
    "ex2.csv",
    names=names,
    index_col="message"
)
# creates DataFrame w 'message' as index
'''
         a   b   c   d
message
hello    1   2   3   4
world    5   6   7   8
foo      9  10  11  12
'''
pd.read_csv(
    "ex2.csv",
    names=["a","b","c","d","message"],
    index_col=["a","message"]
)
# hierarchical index from the index_col arg
'''
            b   c   d
a message
1 hello     2   3   4
5 world     6   7   8
9 foo      10  11  12
'''
parsed=pd.read_csv(
    "csv_mindex.csv",
    index_col=["key1","key2"]
); parsed
# hierarchical index
'''
           value1  value2
key1 key2
one  a          1       2
     b          3       4
     c          5       6
     d          7       8
two  a          9      10
     b         11      12
     c         13      14
     d         15      16
'''
