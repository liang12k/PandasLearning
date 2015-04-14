"""
merge, join operations:
-combine data sets by linking rows using 1+ keys
 ^ central to relational databases

**note: defaults merge
-on overlapping col names as keys
-inner join: intersection of keys
-outer join: union of keys
-left, right join: respective of tables left,right
"""

import pandas as pd

# dict keys are the col names
# dict vals are the col vals
df1=pd.DataFrame(
    {
        "key":list("bbacaab"),
        "data1":range(7)
    }
)
df2=pd.DataFrame(
    {
        "key":list("abd"),
        "data2":range(3)
    }
)
print df1
'''
   data1 key
0      0   b
1      1   b
2      2   a
3      3   c
4      4   a
5      5   a
6      6   b
'''
print df2
'''
   data2 key
0      0   a
1      1   b
2      2   d
'''
# # many-to-one merge situation
# # default merge on overlapping col names as keys
print pd.merge(df1,df2)
# merge on 'key' col; alike col name
# **note: merge on like 'key' vals
'''
   data1 key  data2
0      0   b      1
1      1   b      1
2      6   b      1
3      2   a      0
4      4   a      0
5      5   a      0
'''
# same as: pd.merge(df1,df2,on="key")
print pd.merge(df1,df2)==pd.merge(df1,df2,on="key")
'''
  data1   key data2
0  True  True  True
1  True  True  True
2  True  True  True
3  True  True  True
4  True  True  True
5  True  True  True
'''
df3=pd.DataFrame(
    {
        "lkey":list("bbacaab"),
        "data1":range(7)
    }
)
df4=pd.DataFrame(
    {
        "rkey":list("abd"),
        "data2":range(3)
    }
)
print df3
'''
   data1 lkey
0      0    b
1      1    b
2      2    a
3      3    c
4      4    a
5      5    a
6      6    b
'''
print df4
'''
   data2 rkey
0      0    a
1      1    b
2      2    d
'''
print pd.merge(df3,df4,left_on="lkey",right_on="rkey")
# merge on like lkey,rkey vals
#
# **note: mergeerror on no common col names
# pd.merge(df3,df4)
# MergeError: No common columns to perform merge on
'''
   data1 lkey  data2 rkey
0      0    b      1    b
1      1    b      1    b
2      6    b      1    b
3      2    a      0    a
4      4    a      0    a
5      5    a      0    a
'''
print pd.merge(df1,df2,how="outer")
# outer join is a union of values
# overlapping 'key' col name;
# **note: NaN val for DNEs
# 'key' val 'd' DNE in 'data1',
# 'c' DNE in 'data2'
'''
   data1 key  data2
0      0   b      1
1      1   b      1
2      6   b      1
3      2   a      0
4      4   a      0
5      5   a      0
6      3   c    NaN
7    NaN   d      2
'''
