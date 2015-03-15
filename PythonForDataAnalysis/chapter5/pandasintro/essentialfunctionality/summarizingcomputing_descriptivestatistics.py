"""
reductions, summary statistics
-methods that extract a single value
 from Series or Series of values from
 rows or cols of a DataFrame
"""

import numpy as np
import pandas as pd

df=pd.DataFrame(
    [[1.4,np.nan],[7.1,-4.5],
     [np.nan,np.nan],[0.75,-1.3]],
    index=list("abcd"),
    columns=["one","two"]
)
df
#     one  two
# a  1.40  NaN
# b  7.10 -4.5
# c   NaN  NaN
# d  0.75 -1.3
#
# df.fillna(99)
#      one   two
# a   1.40  99.0
# b   7.10  -4.5
# c  99.00  99.0
# d   0.75  -1.3
#
df.sum()
# sum of all col values per col
#
# one    9.25
# two   -5.80
# dtype: float64
df.sum(1)
# sum of all row values per row
# a    1.40
# b    2.60
# c     NaN
# d   -0.55
# dtype: float64
df.mean(axis=1, skipna=False)
# a      NaN
# b    1.300
# c      NaN
# d   -0.275
# dtype: float64
df.mean(axis=1)
# a    1.400
# b    1.300
# c      NaN
# d   -0.275
# dtype: float64

# # Table5-9: operations for reduction methods
{'axis': "Axis to reduce over. 0 for DataFrame's rows and 1 for columns.",
 'level': 'Reduce grouped by level if the axis is hierarchically-indexed (MultiIndex).',
 'skipna': 'Exclude missing values, True by default.'}

# # indirect statistics returned
df.idxmax()
# index value of max value is
#
# one    b
# two    d
# dtype: object
df.idxmax(1)
# a    one
# b    one
# c    NaN
# d    one
# dtype: object
df.idxmin()
# index value of min value
#
# one    d
# two    b
# dtype: object
df.idxmin(1)
# a    one
# b    two
# c    NaN
# d    two
# dtype: object
#
# # accumulations
df.cumsum()
# reminder: next value is the sum of it
# and the previous value
#
#     one  two
# a  1.40  NaN
# b  8.50 -4.5
# c   NaN  NaN
# d  9.25 -5.8
#
df.describe()
# get general summary statistics
#
#             one       two
# count  3.000000  2.000000
# mean   3.083333 -2.900000
# std    3.493685  2.262742
# min    0.750000 -4.500000
# 25%    1.075000 -3.700000
# 50%    1.400000 -2.900000
# 75%    4.250000 -2.100000
# max    7.100000 -1.300000
df
#     one  two
# a  1.40  NaN
# b  7.10 -4.5
# c   NaN  NaN
# d  0.75 -1.3
#
# # non-numeric data
obj=pd.Series(["a","a","b","c"]*4)
obj.describe()
# count     16
# unique     3
# top        a
# freq       8
# dtype: object
obj.value_counts()
# a    8
# b    4
# c    4
# dtype: int64

# # Table5-10: Descriptive & Summary Statistics
