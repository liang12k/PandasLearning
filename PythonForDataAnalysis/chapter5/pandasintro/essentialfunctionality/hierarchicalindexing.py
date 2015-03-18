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
data.index
'''
MultiIndex(
    levels=[[u'a', u'b', u'c', u'd'], [1, 2, 3]],
    labels=[[0, 0, 0, 1, 1, 1, 2, 2, 3, 3], 
            [0, 1, 2, 0, 1, 2, 0, 1, 1, 2]])
'''
# # site w multiindex examples
# # http://assorted-experience.blogspot.com/2013/05/multi-indexing-with-pandas-dataframe.html
