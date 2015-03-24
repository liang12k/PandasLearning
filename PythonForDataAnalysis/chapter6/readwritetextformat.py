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
