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
