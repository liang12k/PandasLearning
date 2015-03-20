"""
hierarchical indexing:
-enables multiple index levels (2+) on an axis
 provides a way to work w higher dimensional data
 in lower dimensional form

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
# # -in this case, level 2
#
# a    0.735823
# b    0.161846
# c   -0.203287
# d   -1.665426
# dtype: float64
