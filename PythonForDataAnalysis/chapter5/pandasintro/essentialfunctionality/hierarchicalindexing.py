"""
Hierarchical Indexing:
-enables multiple index levels (2+) on an axis
 provides a way to work w higher dimensional data
 in lower dimensional form
- .unstack: reshapes data to get a DataFrame
  : .stack applied on .unstack gets 
    original data form (inverse operation)

MultiIndex indexing:
-http://pandas.pydata.org/pandas-docs/dev/advanced.html
-aka: multi-level indexing
-obj is an array of tuples and each tuple is unique
-site w examples: http://assorted-experience.blogspot.com/2013/05/multi-indexing-with-pandas-dataframe.html
"""

import numpy as np
from numpy import nan as NA
from pandas import Series, DataFrame

# # series w MultiIndex as index
data=Series(
    np.random.randn(10), # rand values
    index=[
        list("aaabbbccdd"), # 'parent' index
        [1,2,3,1,2,3,1,2,2,3] # 'child' index
    ]
)
data
# 'nested' index
'''
a  1    0.994479
   2   -0.849546
   3   -0.126639
b  1   -0.677520
   2    0.519697
   3    0.187125
c  1    0.430335
   2   -0.479693
d  2    0.614288
   3   -0.804458
dtype: float64
'''
data.a
# 1   -0.521040
# 2    0.735823
# 3    0.893494
# dtype: float64
data.a[1] # == data['a'][1]
# -0.5210397174321687
data.index
'''
MultiIndex(
    levels=[[u'a', u'b', u'c', u'd'], [1, 2, 3]],
    labels=[[0, 0, 0, 1, 1, 1, 2, 2, 3, 3], 
            [0, 1, 2, 0, 1, 2, 0, 1, 1, 2]])
'''
# # site w multiindex examples
# # http://assorted-experience.blogspot.com/2013/05/multi-indexing-with-pandas-dataframe.html
data["b":"c"]
'''
b  1   -1.725485
   2    0.161846
   3    0.394919
c  1    0.565266
   2   -0.203287
dtype: float64
'''
data.ix["b"]
# 1   -1.725485
# 2    0.161846
# 3    0.394919
# dtype: float64
data.ix[["b","d","a"]]
'''
b  1   -1.725485
   2    0.161846
   3    0.394919
d  2   -1.665426
   3    0.578462
a  1   -0.521040
   2    0.735823
   3    0.893494
dtype: float64
'''
data[:,2]
# # data selection from inner level
# # -in this case, each 'parent' level 2 (row 2)
#
# a    0.735823
# b    0.161846
# c   -0.203287
# d   -1.665426
# dtype: float64
data[:,3]
# values of each 'parent' index's row 3
#
# a    0.893494
# b    0.394919
# d    0.578462
# dtype: float64

# # reshaping data
data.unstack() # gets a DataFrame
'''
          1         2         3
a -0.521040  0.735823  0.893494
b -1.725485  0.161846  0.394919
c  0.565266 -0.203287       NaN
d       NaN -1.665426  0.578462
'''
# inverse of .unstack is .stack
data.unstack().stack()
'''
a  1   -0.521040
   2    0.735823
   3    0.893494
b  1   -1.725485
   2    0.161846
   3    0.394919
c  1    0.565266
   2   -0.203287
d  2   -1.665426
   3    0.578462
dtype: float64
'''

# # DataFrame: either axis can have
#              hierarchical index
frame=DataFrame(
    np.arange(12).reshape((4,3)),
    index=[
        list("aabb"),
        [1,2,1,2]
    ],
    columns=[
        ["Ohio","Ohio","Colorado"],
        ["Green","Red","Green"]
    ]
)
# parent row index: 'a','b'
# -with sub rows: 1,2 , 1,2
# column names: 'Ohio','Colorado'
# -with sub cols: 'Green','Red' , 'Green'
#  **note: Ohio displayed once, owns 2 cols
frame
'''
     Ohio     Colorado
    Green Red    Green
a 1     0   1        2
  2     3   4        5
b 1     6   7        8
  2     9  10       11
'''
# data selection, diving into MultiIndex
frame.Ohio
'''
     Green  Red
a 1      0    1
  2      3    4
b 1      6    7
  2      9   10
'''
frame.Ohio["Green"]
'''
a  1    0
   2    3
b  1    6
   2    9
Name: Green, dtype: int64
'''
frame.Ohio["Green"]["b"]
'''
1    6
2    9
Name: Green, dtype: int64
'''
frame.Ohio["Green"][:,2]
# all rows of 'Green', take row 2
'''
a    0
b    6
Name: Green, dtype: int64
'''
# assigning index names
# **note: not axis labels!!
frame.index.names=["key1","key2"]
frame.columns.names=["state","color"]
frame
'''
state      Ohio     Colorado
color     Green Red    Green
key1 key2
a    1        0   1        2
     2        3   4        5
b    1        6   7        8
     2        9  10       11
'''
frame.Ohio
# partial col indexing
'''
color      Green  Red
key1 key2
a    1         0    1
     2         3    4
b    1         6    7
     2         9   10
'''
frame.unstack()
# rearrange the DataFrame
'''
state  Ohio            Colorado
color Green    Red        Green
key2      1  2   1   2        1   2
key1
a         0  3   1   4        2   5
b         6  9   7  10        8  11
'''
# construct columns frame's cols into MultiIndex
(pd.MultiIndex
   .from_arrays(
       [
           ["Ohio","Ohio","Colorado"],
           ["Green","Red","Green"]
       ],
       names=["state","color"])

)
'''
MultiIndex(
levels=[[u'Colorado', u'Ohio'], [u'Green', u'Red']],
labels=[[1, 1, 0], [0, 1, 0]],
names=[u'state', u'color'])
'''
