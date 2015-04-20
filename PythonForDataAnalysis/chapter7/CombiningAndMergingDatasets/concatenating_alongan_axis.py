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
# # **note: concat on Series or DataFrame with axis=1
# # hierarchical keys becaome DataFrame column
# print pd.concat([s1,s2,s3],axis=1,keys=["one","two","three"])
'''
   one  two  three
a    0  NaN    NaN
b    1  NaN    NaN
c  NaN    2    NaN
d  NaN    3    NaN
e  NaN    4    NaN
f  NaN  NaN      5
g  NaN  NaN      6
'''
df1=pd.DataFrame(
    np.arange(6).reshape(3,2),
    index=list("abc"),
    columns=["one","two"]
)
df2=pd.DataFrame(
    5+np.arange(4).reshape(2,2),
    index=["a","c"],
    columns=["three","four"]
)
# print df1
'''
   one  two
a    0    1
b    2    3
c    4    5
'''
# print df2
'''
   three  four
a      5     6
c      7     8
'''
# print pd.concat([df1,df2],axis=1,keys=["level1","level2"])
# **note: axis=1 : keys are the col hierarchical index
'''
  level1     level2
     one two  three four
a      0   1      5    6
b      2   3    NaN  NaN
c      4   5      7    8
'''
# print pd.concat([df1,df2],keys=["level1","level2"])
'''
          four  one  three  two
level1 a   NaN    0    NaN    1
       b   NaN    2    NaN    3
       c   NaN    4    NaN    5
level2 a     6  NaN      5  NaN
       c     8  NaN      7  NaN
'''
# print pd.concat({"level1":df1,"level2":df2},axis=1)
# passing in dict of objs, dict keys used for keys
'''
  level1     level2
     one two  three four
a      0   1      5    6
b      2   3    NaN  NaN
c      4   5      7    8
'''
# print pd.concat([df1,df2],axis=1,keys=["level1","level2"],names=["upper","lower"])
# naming upper,lower hierarchical indexes
'''
upper level1     level2
lower    one two  three four
a          0   1      5    6
b          2   3    NaN  NaN
c          4   5      7    8
'''
df11=pd.DataFrame(np.random.randn(3,4),columns=list("abcd")) # 3 rows, 4 cols
df22=pd.DataFrame(np.random.randn(2,3),columns=list("bda")) # 2 rows, 3 cols
# print df11
'''
          a         b         c         d
0 -1.385537 -0.673809 -0.327916  0.393996
1  2.798291 -0.510207 -0.629066  0.118758
2 -0.122484 -0.778146  0.571123 -1.043147
'''
# print df22
'''
          b         d         a
0  3.235226 -0.699285  1.386694
1 -1.030489 -0.035350 -2.215457
'''
# print pd.concat([df11,df22],ignore_index=True)
# **note: ignore_index creates the standard index count
'''
          a         b         c         d
0 -1.385537 -0.673809 -0.327916  0.393996
1  2.798291 -0.510207 -0.629066  0.118758
2 -0.122484 -0.778146  0.571123 -1.043147
3  1.386694  3.235226       NaN -0.699285
4 -2.215457 -1.030489       NaN -0.035350
'''
# pd.concat([df11,df22])
# **note: index values are unioned vs ignore_index isn't
'''
          a         b         c         d
0 -1.385537 -0.673809 -0.327916  0.393996
1  2.798291 -0.510207 -0.629066  0.118758
2 -0.122484 -0.778146  0.571123 -1.043147
0  1.386694  3.235226       NaN -0.699285
1 -2.215457 -1.030489       NaN -0.035350
'''

# # Table7-2: .concat function arguments
{'axis': 'Axis to concatenate along; defaults to 0',
 'ignore_index': 'Do not preserve indexes along concatenation axis, instead producing a new range(total_length) index',
 'join': "One of 'inner', 'outer', defaulting to 'outer'; whether to intersection (inner) or union (outer) together indexes along the other axes",
 'join_axes': 'Specific indexes to use for the other n-1 axes instead of performing union/intersection logic',
 'keys': 'Values to associate with objects being concatenated, forming a hierarchical index along the concatenation axis. Can either be a list or array of arbitrary values, an array of tuples, or a list of arrays (if multiple level arrays passed in levels)',
 'levels': 'Specific indexes to use as hierarchical index level or levels if keys passed names Names for created hierarchical levels if keys and / or levels passed',
 'objs': 'List or dict of pandas objects to be concatenated. The only required argument',
 'verify_integrity': 'Check new axis in concatenated object for duplicates and raise exception if so. By default (False) allows duplicates'}
