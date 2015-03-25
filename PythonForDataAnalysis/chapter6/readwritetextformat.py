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

# # no delimiter in txt file
# # determine if it can be delimited by whitespace
list(open("ex3.txt"))
'''
['            A         B         C\n',
 'aaa -0.264438 -1.026059 -0.619500\n',
 'bbb  0.927272  0.302904 -0.032399\n',
 'ccc -0.264273 -0.386314 -0.217601\n',
 'ddd -0.871858 -0.348382  1.100491\n']
'''
result=pd.read_table("ex3.txt",sep="\s+"); result
# **note: since there's 1 less named col,
#         .read_table places 1st col as index
'''
            A         B         C
aaa -0.264438 -1.026059 -0.619500
bbb  0.927272  0.302904 -0.032399
ccc -0.264273 -0.386314 -0.217601
ddd -0.871858 -0.348382  1.100491
'''
result.index
# Index([u'aaa', u'bbb', u'ccc', u'ddd'], dtype='object')

# # skipping rows from read file
list(open("ex4.csv"))
# misc rows below, should be skipped when loaded
'''
['# hey!\n',
 'a,b,c,d,message\n',
 '# just wanted to make things more difficult for you\n',
 '# who reads CSV files with computers, anyway?\n',
 '1,2,3,4,hello\n',
 '5,6,7,8,world\n',
 '9,10,11,12,foo']
'''
pd.read_csv(
    "ex4.csv",
    skiprows=[0,2,3],
    index_col="message"
)
'''
         a   b   c   d
message
hello    1   2   3   4
world    5   6   7   8
foo      9  10  11  12
'''

# # handling missing values
# # -empty sting, marked sentinel value
# # -pandas default values are: NA, -1.#IND, NULL
list(open("ex5.csv"))
'''
['something,a,b,c,d,message\n',
 'one,1,2,3,4,NA\n',
 'two,5,6,,8,world\n',
 'three,9,10,11,12,foo']
'''
result=pd.read_csv("ex5.csv"); result
'''
  something  a   b   c   d message
0       one  1   2   3   4     NaN
1       two  5   6 NaN   8   world
2     three  9  10  11  12     foo
'''
pd.isnull(result)
'''
  something      a      b      c      d message
0     False  False  False  False  False    True
1     False  False  False   True  False   False
2     False  False  False  False  False   False
'''
pd.notnull(result)
'''
  something     a     b      c     d message
0      True  True  True   True  True   False
1      True  True  True  False  True    True
2      True  True  True   True  True    True
'''
result=pd.read_csv("ex5.csv",na_values=["NULL"])
result
'''
  something  a   b   c   d message
0       one  1   2   3   4     NaN
1       two  5   6 NaN   8   world
2     three  9  10  11  12     foo
'''
# # ** note: pd.read_csv("ex5.csv") != result
# # this is True though:
# pd.read_csv("ex5.csv").isnull()==result.isnull()
'''
  something     a     b      c     d message
0      True  True  True   True  True   False
1      True  True  True  False  True    True
2      True  True  True   True  True    True
'''
### # ***** ?????????? **********************
# # strange, needs investigation
# r=pd.read_csv("ex5.csv",na_values=["NULL"])
# r==result:
'''
  something     a     b      c     d message
0      True  True  True   True  True   False
1      True  True  True  False  True    True
2      True  True  True   True  True    True
'''
# r=pd.read_csv("ex5.csv")
# r==pd.read_csv("ex5.csv")
'''
  something     a     b      c     d message
0      True  True  True   True  True   False
1      True  True  True  False  True    True
2      True  True  True   True  True    True
'''

# # specifying different sentinels
# # -certain values are NaN
sentinels={
    "message":["foo","NA"],
    "something" : ["two"]
}
srslt=pd.read_csv("ex5.csv", na_values=sentinels)
srslt
'''
  something  a   b   c   d message
0       one  1   2   3   4     NaN
1       NaN  5   6 NaN   8   world
2     three  9  10  11  12     NaN
'''

# # Table6-2: .read_csv, .read_table func args
{'chunksize': 'For iteration, size of file chunks',
 'comment': 'Character or characters to split comments off the end of lines',
 'converters': "Dict containing column number of name mapping to functions. For example {'foo': f} would apply\nthe function f to all values in the 'foo' column",
 'date_parser': 'Function to use to parse dates',
 'dayfirst': 'When parsing potentially ambiguous dates, treat as international format (e.g. 7/6/2012 -> June 7,2012). Default False',
 'encoding': "Text encoding for unicode. For example 'utf-8' for UTF-8 encoded text",
 'header': 'Row number to use as column names. Defaults to 0 (first row), but should be None if there is no header row',
 'index_col': 'Column numbers or names to use as the row index in the result. Can be a single name/number or a list of them for a hierarchical index',
 'iterator': 'Return a TextParser object for reading file piecemeal',
 'keep_date_col': 'If joining columns to parse date, drop the joined columns. Default True',
 'na_values': 'Sequence of values to replace with NA',
 'names': 'List of column names for result, combine with header=None',
 'nrows': 'Number of rows to read from beginning of file',
 'parse_dates': 'Attempt to parse data to datetime; False by default. If True, will attempt to parse all columns. Otherwise can specify a list of column numbers or name to parse. If element of list is tuple or list, will combine multiple columns together and parse to date (for example if date/time split across two columns)',
 'path': 'String indicating filesystem location, URL, or file-like object',
 'sep or delimiter': 'Character sequence or regular expression to use to split fields in each row',
 'skip_footer': 'Number of lines to ignore at end of file',
 'skiprows': 'Number of rows at beginning of file to ignore or list of row numbers (starting from 0) to skip',
 'squeeze': 'If the parsed data only contains one column return a Series',
 'thousands': "Separator for thousands, e.g. ',' or '.'",
 'verbose': 'Print various parser output information, like the number of missing values placed in non-numeric columns'}
