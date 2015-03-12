"""
arithmetic between objects with different indexes
-note: adding together objects w different 
       index pairs will result in union of 
       index pairs

internal data alignment introduces NA values in
indicies that don't overlap
-missing values propagate in arithmetic operations
"""

import numpy as np
import pandas as pd
# from string import ascii_lowercase

s1=pd.Series(
    [7.3,-2.5,3.4,1.5],
    # index=[_ for _ in ascii_lowercase[:4]],
    index=["a","c","d","e"]
)
s2=pd.Series(
    [-2.1,3.6,-1.5,4,3.1],
    index=["a","c","e","f","g"]
)
s1
# a    7.3
# c   -2.5
# d    3.4
# e    1.5
# dtype: float64
s2
# a   -2.1
# c    3.6
# e   -1.5
# f    4.0
# g    3.1
# dtype: float64
s1+s2
# a    5.2
# c    1.1
# d    NaN
# e    0.0
# f    NaN
# g    NaN
# dtype: float64

# # internal data alignment and NA values
df1=pd.DataFrame(
    np.arange(9.).reshape((3,3)),
    columns=list("bcd"),
    index=["Ohio","Texas","Colorado"],
)
df2=pd.DataFrame(
    np.arange(12.).reshape((4,3)),
    columns=list("bde"),
    index=["Utah","Ohio","Texas","Oregon"]
)
df1
#           b  c  d
# Ohio      0  1  2
# Texas     3  4  5
# Colorado  6  7  8
df2
#         b   d   e
# Utah    0   1   2
# Ohio    3   4   5
# Texas   6   7   8
# Oregon  9  10  11
#
# # union of dataframes
df1+df2
#
# rows: 'Utah','Oregon','Colorado' DNE in both
# cols: 'c','e' DNE in both
# 
#            b   c   d   e
# Colorado NaN NaN NaN NaN
# Ohio       3 NaN   6 NaN
# Oregon   NaN NaN NaN NaN
# Texas      9 NaN  12 NaN
# Utah     NaN NaN NaN NaN

# # arithmetic methos with fill values
df1=pd.DataFrame(
    np.arange(12.).reshape((3,4)),
    columns=list("abcd")
)
df2=pd.DataFrame(
    np.arange(20.).reshape((4,5)),
    columns=list("abcde")
)
df1
#    a  b   c   d
# 0  0  1   2   3
# 1  4  5   6   7
# 2  8  9  10  11
df2
#     a   b   c   d   e
# 0   0   1   2   3   4
# 1   5   6   7   8   9
# 2  10  11  12  13  14
# 3  15  16  17  18  19
#
# default: NaN values as filled
df1+df2
#     a   b   c   d   e
# 0   0   2   4   6 NaN
# 1   9  11  13  15 NaN
# 2  18  20  22  24 NaN
# 3 NaN NaN NaN NaN NaN
#
# .add: fill_value param to fill in default value
df1.add(df2,fill_value=0)
#
# df1 - 'e' col,'3' row of 0 values
# 
#     a   b   c   d   e
# 0   0   2   4   6   4
# 1   9  11  13  15   9
# 2  18  20  22  24  14
# 3  15  16  17  18  19
#
# # if filling in df1+df2 NaN w value
(df1+df2).fillna(value=0.0)
#     a   b   c   d  e
# 0   0   2   4   6  0
# 1   9  11  13  15  0
# 2  18  20  22  24  0
# 3   0   0   0   0  0

