"""
merge keys of DataFrame can be found in its index
left_index=True,right_index=True
indivually or both to indicate index used as merge key

# http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.merge.html
"""

import pandas as pd

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
