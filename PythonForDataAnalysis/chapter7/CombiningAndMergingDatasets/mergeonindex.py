"""
merge keys of DataFrame can be found in its index
left_index=True,right_index=True
indivually or both to indicate index used as merge key

# http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.merge.html
"""

import pandas as pd
import numpy as np

left1=pd.DataFrame(
    {
        "key":list("abaabc"),
        "value":range(6)
    }
)
right1=pd.DataFrame(
    {"group_val":[3.5,7]},
    index=["a","b"]
)
# print left1
'''
  key  value
0   a      0
1   b      1
2   a      2
3   a      3
4   b      4
5   c      5
'''
# print right1
'''
   group_val
a        3.5
b        7.0
'''
# print pd.merge(left1,right1,left_on="key",right_index=True)
# merge on left1 'key' col, using right1 index col vals
# which is ['a','b'] since there's no common col name
'''
  key  value  group_val
0   a      0        3.5
2   a      2        3.5
3   a      3        3.5
1   b      1        7.0
4   b      4        7.0
'''
# print pd.merge(left1,right1,left_on="key",right_index=True,how="outer")
# using common col vals of left1 'key' col and
# right1 index vals, get an outer join (union) result
'''
  key  value  group_val
0   a      0        3.5
2   a      2        3.5
3   a      3        3.5
1   b      1        7.0
4   b      4        7.0
5   c      5        NaN
'''
# # hierarchically-indexed data
lefth=pd.DataFrame(
    {
        "key1":["Ohio"]*3+["Nevada"]*2,
        "key2":[2000,2001,2002,2001,2002],
        "data":np.arange(5.)
    }
)
righth=pd.DataFrame(
    # 6 rows, 2 cols
    np.arange(12).reshape((6,2)),
    index=[
        ["Nevada"]*2+["Ohio"]*4,
        [2001,2000,2000,2000,2001,2002]
    ],
    columns=["event1","event2"]
)
print lefth
'''
   data    key1  key2
0     0    Ohio  2000
1     1    Ohio  2001
2     2    Ohio  2002
3     3  Nevada  2001
4     4  Nevada  2002
'''
print righth
'''
             event1  event2
Nevada 2001       0       1
       2000       2       3
Ohio   2000       4       5
       2000       6       7
       2001       8       9
       2002      10      11
'''
# print pd.merge(lefth,righth,left_on=["key1","key2"],right_index=True)
# lefth 'key1','key2' cols share values with
# righth multiindex index values
'''
   data    key1  key2  event1  event2
0     0    Ohio  2000       4       5
0     0    Ohio  2000       6       7
1     1    Ohio  2001       8       9
2     2    Ohio  2002      10      11
3     3  Nevada  2001       0       1
'''
# print pd.merge(lefth,righth,left_on=["key1","key2"],right_index=True,how="outer")
# outer join to see union
'''
   data    key1  key2  event1  event2
0     0    Ohio  2000       4       5
0     0    Ohio  2000       6       7
1     1    Ohio  2001       8       9
2     2    Ohio  2002      10      11
3     3  Nevada  2001       0       1
4     4  Nevada  2002     NaN     NaN
4   NaN  Nevada  2000       2       3
'''
# print pd.merge(lefth,righth,left_on=["key1","key2"],right_index=True,how="left")
# to join on all lefth 'key1','key2' col vals
# **note: NaN for righth values where Nevada,2002 DNE
'''
   data    key1  key2  event1  event2
0     0    Ohio  2000       4       5
0     0    Ohio  2000       6       7
1     1    Ohio  2001       8       9
2     2    Ohio  2002      10      11
3     3  Nevada  2001       0       1
4     4  Nevada  2002     NaN     NaN
'''
