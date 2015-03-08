"""
.reindex - operating on pandas objects
           create new object with data conformed
           to a new index
         - 'method' arg to handle interpolation

interpolation w blank values
http://peltiertech.com/mind-the-gap-charting-empty-cells/
-tl;dr: best to leave empty values as is
        -setting as 0s is deceptable as this 
         is a value
        -if plotting: 1. skip it, 2. leave as NaN
"""

import pandas as pd
import numpy as np

obj=pd.Series(
    [4.5,7.2,-5.3,3.6],
    index=["d","b","a","c"]
)
obj
# d    4.5
# b    7.2
# a   -5.3
# c    3.6
# dtype: float64
#
# # pd.Series.reindex rearranges data according
# # to new index
# # missing values introduced for DNE index values
#
# 'e' index DNE 
obj2=obj.reindex(["a","b","c","d","e"])
obj2
# a   -5.3
# b    7.2
# c    3.6
# d    4.5
# e    NaN
# dtype: float64
#
# fill in NaN values of reindex
obj.reindex(
    obj2.index,
    fill_value=0
)
# a   -5.3
# b    7.2
# c    3.6
# d    4.5
# e    0.0
# dtype: float64

# # ordered data (ie: time series)
# # do some interpolation (alter data by
# # inserting new data), filling of values
# # when reindexing
# # 'method' arg option allows filling holes in
# # reindexed data - methods are:
# # -ffill, pad : fill, carry values forward
# # -bfill, backfill: fill, carry values backward
#
obj3=pd.Series(
    ["blue","purple","yellow"],
    index=[0,2,4]
)
obj3.reindex(range(6))
# 0      blue
# 1       NaN
# 2    purple
# 3       NaN
# 4    yellow
# 5       NaN
# dtype: object
#
# # taking the latest value before blank NaN index value
# # plug into NaN
obj3ffill=obj3.reindex(range(6),method="ffill")
# 0      blue
# 1      blue
# 2    purple
# 3    purple
# 4    yellow
# 5    yellow
# dtype: object
#
# # taking latest value after blank NaN index value
# # plug into NaN
obj3bfill=obj3.reindex(range(6),method="bfill")
# 0      blue
# 1    purple
# 2    purple
# 3    yellow
# 4    yellow
# 5       NaN
# dtype: object

# #
# # Table5-4
# # .reindex 'method' (interpolation) arg options
# # 
# ffill, pad - fill, carry values forward
#              taking latest value before blank NaN
#              value, plug that into NaN
# bfill, backfill - fill, carry values backward
#                   taking latest value after blank NaN
#                   value, plug that into NaN

# # reindex DataFrames
# # -can alter row, col, or both
# # -by default, rows are reindexed in result
frame=pd.DataFrame(
    np.arange(9).reshape((3,3)),
    index=["a","c","d"],
    columns=["Ohio","Texas","California"]
)
frame
 #    Ohio  Texas  California
 # a     0      1           2
 # c     3      4           5
 # d     6      7           8
#
from string import ascii_lowercase
frame2=frame.reindex(
    [_ for _ in ascii_lowercase[:4]]
)
# ^ same as:
# frame2=frame.reindex(["a","b","c","d"])
frame2
#    Ohio  Texas  California
# a     0      1           2
# b   NaN    NaN         NaN
# c     3      4           5
# d     6      7           8
#
# # reindex using 'columns' keyword
states=["Texas","Utah","California"]
# 'Utah' col doesn't exist, col will be NaN values
frame.reindex(columns=states)
#    Texas  Utah  California
# a      1   NaN           2
# c      4   NaN           5
# d      7   NaN           8
#
# # ^ reindex in single call
# #   where interpolation happens row-wise (axis=0)
frame.reindex(
    index=frame2.index,
    method="ffill",
    columns=states
)
   #    Texas  Utah  California
   # a      1   NaN           2
   # b      1   NaN           2
   # c      4   NaN           5
   # d      7   NaN           8
#
# # note: succinct label-indexing reindex
frame.ix[
    frame2.index,
    states
]
   #    Texas  Utah  California
   # a      1   NaN           2
   # b    NaN   NaN         NaN
   # c      4   NaN           5
   # d      7   NaN           8
#

# #
# # Table5-5
# # reindex function args
# #
{'copy': 'Do not copy underlying data if new index is equivalent to old index. True by default (i.e. always copy data).',
 'fill_value': 'Substitute value to use when introducing missing data by reindexing',
 'index': 'New sequence to use as index. Can be Index instance or any other sequence-like Python data structure. An Index will be used exactly as is without any copying',
 'level': 'Match simple Index on level of MultiIndex, otherwise select subset of',
 'limit': 'When forward- or backfilling, maximum size gap to fill (how many to fill instead of all)',
 'method': 'Interpolation (fill) method, see Table 5-4 for options. (ffill,bfill)'}
