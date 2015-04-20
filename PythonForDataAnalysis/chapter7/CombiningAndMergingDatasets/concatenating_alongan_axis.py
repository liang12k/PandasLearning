"""
numpy.concatenate:
-data combination with raw numpy arrays


"""

import numpy as np
import pandas as pd

arr=np.arange(12).reshape((3,4))
# print arr
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''
# print np.concatenate([arr,arr],axis=1)
'''
[[ 0  1  2  3  0  1  2  3]
 [ 4  5  6  7  4  5  6  7]
 [ 8  9 10 11  8  9 10 11]]
'''
s1=pd.Series([0,1],index=["a","b"])
s2=pd.Series([2,3,4],index=["c","d","e"])
s3=pd.Series([5,6],index=["f","g"])
# print pd.concat([s1,s2,s3])
# default concat on index 0
'''
a    0
b    1
c    2
d    3
e    4
f    5
g    6
dtype: int64
'''
# print pd.concat([s1,s2,s3],axis=1)
# axis=1 is cols; no overlap of cols in union
'''
    0   1   2
a   0 NaN NaN
b   1 NaN NaN
c NaN   2 NaN
d NaN   3 NaN
e NaN   4 NaN
f NaN NaN   5
g NaN NaN   6
'''
s4=pd.concat([s1*5,s3])
# print s4
'''
a    0
b    5
f    5
g    6
dtype: int64
'''
# print pd.concat([s1,s4],axis=1)
'''
    0  1
a   0  0
b   1  5
f NaN  5
g NaN  6
'''
# print pd.concat([s1,s4])
# defaults to axis=0 (rows)
# -**notice the duplicate index values
'''
a    0
b    1
a    0
b    5
f    5
g    6
dtype: int64
'''
# print pd.concat([s1,s4],axis=1,join="inner")
# only on same index values
'''
   0  1
a  0  0
b  1  5
'''
# print pd.concat([s1,s4],axis=1,join_axes=[list("acbe")])
# specify axes to join (in this case, axis=1, cols)
'''
    0   1
a   0   0
c NaN NaN
b   1   5
e NaN NaN
'''
# # hierarchical index on concat axis
result=pd.concat([s1,s1,s3],keys=["one","two","three"])
# print s1
'''
a    0
b    1
dtype: int64
'''
# print s3
'''
f    5
g    6
dtype: int64
'''
# print result
# allots keys for each DataFrame
'''
one    a    0
       b    1
two    a    0
       b    1
three  f    5
       g    6
dtype: int64
'''
# print result.unstack()
# converts result back to 2D DataFrame
'''
        a   b   f   g
one     0   1 NaN NaN
two     0   1 NaN NaN
three NaN NaN   5   6
'''
# print pd.concat([s1,s2,s4],keys=["one","two","three"])
'''
one    a    0
       b    1
two    c    2
       d    3
       e    4
three  a    0
       b    5
       f    5
       g    6
dtype: int64
'''
