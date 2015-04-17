"""
merge keys of DataFrame can be found in its index
left_index=True,right_index=True
indivually or both to indicate index used as merge key

# http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.merge.html

.join: default join using index values as left-join
-alternative to .concat of DataFrames
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
# print left1.join(right1,on="key")
# **note: defaults to left-join
'''
  key  value  group_val
0   a      0        3.5
1   b      1        7.0
2   a      2        3.5
3   a      3        3.5
4   b      4        7.0
5   c      5        NaN
'''
# print left1.join(right1)
# **note: unknown what col to left-join on
'''
  key  value  group_val
0   a      0        NaN
1   b      1        NaN
2   a      2        NaN
3   a      3        NaN
4   b      4        NaN
5   c      5        NaN
'''
# print right1.join(left1)
# **note: unknow what col to left-join on
'''
   group_val  key  value
a        3.5  NaN    NaN
b        7.0  NaN    NaN
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
left2=pd.DataFrame(
    [[1.,2.],[3.,4.],[5.,6.]],
    index=list("ace"),
    columns=["Ohio","Nevada"]
)
right2=pd.DataFrame(
    [[7.,8.],[9.,10.],[11.,12.],[13,14]],
    index=list("bcde"),
    columns=["Missouri","Alabama"]
)
# print left2
'''
   Ohio  Nevada
a     1       2
c     3       4
e     5       6
'''
# print right2
'''
   Missouri  Alabama
b         7        8
c         9       10
d        11       12
e        13       14
'''
# print pd.merge(left2,right2,how="outer",left_index=True,right_index=True)
# using index values of left2, right2
# merge on like vals, outer-join (union)
'''
   Ohio  Nevada  Missouri  Alabama
a     1       2       NaN      NaN
b   NaN     NaN         7        8
c     3       4         9       10
d   NaN     NaN        11       12
e     5       6        13       14
'''
# .join: merging on keys (by default)
# print left2.join(right2,how="outer")
'''
   Ohio  Nevada  Missouri  Alabama
a     1       2       NaN      NaN
b   NaN     NaN         7        8
c     3       4         9       10
d   NaN     NaN        11       12
e     5       6        13       14
'''
# # index-on-index merges
# # using .join as an alternative to .concat
another=pd.DataFrame(
    [[7.,8.],[9.,10.],[11.,12.],[16.,17.]],
    index=list("acef"),
    columns=["New York","Oregon"]
)
# print another
'''
   New York  Oregon
a         7       8
c         9      10
e        11      12
f        16      17
'''
# print left2.join([right2,another])
# joining on index values
'''
   Ohio  Nevada  Missouri  Alabama  New York  Oregon
a     1       2       NaN      NaN         7       8
c     3       4         9       10         9      10
e     5       6        13       14        11      12
'''
# print left2.join([right2,another],how="outer")
# joining on index values, union
'''
   Ohio  Nevada  Missouri  Alabama  New York  Oregon
a     1       2       NaN      NaN         7       8
b   NaN     NaN         7        8       NaN     NaN
c     3       4         9       10         9      10
d   NaN     NaN        11       12       NaN     NaN
e     5       6        13       14        11      12
f   NaN     NaN       NaN      NaN        16      17
'''
# print pd.concat([left2,right2,another])
'''
   Alabama  Missouri  Nevada  New York  Ohio  Oregon
a      NaN       NaN       2       NaN     1     NaN
c      NaN       NaN       4       NaN     3     NaN
e      NaN       NaN       6       NaN     5     NaN
b        8         7     NaN       NaN   NaN     NaN
c       10         9     NaN       NaN   NaN     NaN
d       12        11     NaN       NaN   NaN     NaN
e       14        13     NaN       NaN   NaN     NaN
a      NaN       NaN     NaN         7   NaN       8
c      NaN       NaN     NaN         9   NaN      10
e      NaN       NaN     NaN        11   NaN      12
f      NaN       NaN     NaN        16   NaN      17
'''
