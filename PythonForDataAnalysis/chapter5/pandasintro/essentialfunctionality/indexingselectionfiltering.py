"""
.ix - DataFrame label-indexing
      select subset of rows,cols from DataFrame
      with NumPy like notation with axis labels
"""

import numpy as np
import pandas as pd
from string import ascii_lowercase

obj=pd.Series(
    np.arange(4.),
    index=[_ for _ in ascii_lowercase[:4]]
)
obj
# a    0
# b    1
# c    2
# d    3
# dtype: float64
obj["b"]
# 1.0
obj[1]
# 1.0
# obj[2:4]
# c    2
# d    3
# dtype: float64
obj[["b","a","d"]] # specific row order
# b    1
# a    0
# d    3
# dtype: float64
obj[[1,2]] # row specific
# b    1
# c    2
# dtype: float64
obj[obj < 2] # apply filtering on rows
# a    0
# b    1
# dtype: float64
obj["b":"c"] # slicing
# b    1
# c    2
# dtype: float64
obj["b":"c"]=5 # setting value
# a    0
# b    5
# c    5
# d    3
# dtype: float64

# # DataFrame - indexing for retrieving 1+ cols
# #             with either single value or sequence
data=pd.DataFrame(
    np.arange(16).reshape((4,4)),
    index=["Ohio","Colorado","Utah","New York"],
    columns=["one","two","three","four"]
)
data
#           one  two  three  four
# Ohio        0    1      2     3
# Colorado    4    5      6     7
# Utah        8    9     10    11
# New York   12   13     14    15
data["two"]
# Ohio         1
# Colorado     5
# Utah         9
# New York    13
# Name: two, dtype: int64
data[["three","one"]]
#           three  one
# Ohio          2    0
# Colorado      6    4
# Utah         10    8
# New York     14   12
#
# # special cases for indexing
data[:2] # slicing
#           one  two  three  four
# Ohio        0    1      2     3
# Colorado    4    5      6     7
data[data["three"]>5] # filtering (mask)
#           one  two  three  four
# Colorado    4    5      6     7
# Utah        8    9     10    11
# New York   12   13     14    15
#
# # indexing with bool DataFrame
data<5
#             one    two  three   four
# Ohio       True   True   True   True
# Colorado   True  False  False  False
# Utah      False  False  False  False
# New York  False  False  False  False
data[data<5]=0 # assigning 0 to all True vals
#           one  two  three  four
# Ohio        0    0      0     0
# Colorado    0    5      6     7
# Utah        8    9     10    11
# New York   12   13     14    15

# # dataframe .ix
data.ix["Colorado",["two","four"]]
# two     5
# four    7
# Name: Colorado, dtype: int64
#
# select row names, col indices
data.ix[["Colorado","Utah"],[3,0,1]]
#           four  one  two
# Colorado     7    0    5
# Utah        11    8    9
#
# select col "two" w row values up to "Utah"
# Ohio        0
# Colorado    5
# Utah        9
# Name: two, dtype: int64
#
# "three" col values > 5, up to 2 col index
data.ix[data.three>5, :3]
#           one  two  three
# Colorado    0    5      6
# Utah        8    9     10
# New York   12   13     14

# # Table5-6
{'get_value, set_value methods': 'Select single value by row and column label.',
 'icol, irowmethods': 'Select single column or row, respectively, as a Series by integer location.',
 'obj.ix[:, val]': 'Selects single column of subset of columns.',
 'obj.ix[val1, val2]': 'Select both rows and columns.',
 'obj.ix[val]': 'Selects single row of subset of rows from the DataFrame.',
 'obj[val]': 'Select single column or sequence of columns from the DataFrame. Special case con- veniences: boolean array (filter rows), slice (slice rows), or boolean DataFrame (set values based on some criterion).',
 'reindex method': 'Conform one or more axes to new indexes.',
 'xs method': 'Select single row or column as a Series by label.'}
