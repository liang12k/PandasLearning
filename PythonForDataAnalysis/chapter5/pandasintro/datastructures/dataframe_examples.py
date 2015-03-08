"""
DataFrame: tabular, spreadsheet-like data structure
           containing ordered collection of cols
           ^ each col can be diff val (~qztable.Schema)
           has row,col index
           kind of dict of Series (sharing same idx)
           ** data stored as 1D or 2D blocks
"""

import numpy as np
import pandas as pd

# most common DataFrame creation is using
# dict of equal-sized lists or np.array
data={
    "state":["Ohio"]*3+["Nevada"]*2,
    "year":[2000,2001,2002,2001,2002],
    "pop":[1.5,1.7,3.6,2.4,2.9]
}
frame=pd.DataFrame(data)
frame
   #    pop   state  year
   # 0  1.5    Ohio  2000
   # 1  1.7    Ohio  2001
   # 2  3.6    Ohio  2002
   # 3  2.4  Nevada  2001
   # 4  2.9  Nevada  2002

# # specifying sequence of cols (project cols)
pd.DataFrame(data,columns=["year","state","pop"])
   #    year   state  pop
   # 0  2000    Ohio  1.5
   # 1  2001    Ohio  1.7
   # 2  2002    Ohio  3.6
   # 3  2001  Nevada  2.4
   # 4  2002  Nevada  2.9

# # projecting cols that DNE (don't exist)
# # -get NaN vals in cols, no error
frame2=pd.DataFrame(
    data,
    columns=["year","state","pop","debt"],
    index=["one","two","three","four","five"]
)
frame2
   #        year   state  pop debt
   # one    2000    Ohio  1.5  NaN
   # two    2001    Ohio  1.7  NaN
   # three  2002    Ohio  3.6  NaN
   # four   2001  Nevada  2.4  NaN
   # five   2002  Nevada  2.9  NaN
frame2.columns
# Index([u'year', u'state', u'pop', u'debt'], dtype='object')
#
# # selecting specific col name
# # either by df["_col_name_"] or df.colname
# # -note: same indices are used w projections
frame2["state"]
# one        Ohio
# two        Ohio
# three      Ohio
# four     Nevada
# five     Nevada
# Name: state, dtype: object
frame2.year
# one      2000
# two      2001
# three    2002
# four     2001
# five     2002
# Name: year, dtype: int64
#
# # selecting index name
frame2.ix["three"]
# year     2002
# state    Ohio
# pop       3.6
# debt      NaN
# Name: three, dtype: object
#
# # filtering rows
frame2[
    (frame2.year>2001) &
    (frame2.state=="Ohio")
]
#        year state  pop debt
# three  2002  Ohio  3.6  NaN
#
# # modifying cols by assignment
#
# constant scalar value
frame2["debt"]=16.5
frame2
  #        year   state  pop  debt
  # one    2000    Ohio  1.5  16.5
  # two    2001    Ohio  1.7  16.5
  # three  2002    Ohio  3.6  16.5
  # four   2001  Nevada  2.4  16.5
  # five   2002  Nevada  2.9  16.5
#
# assigning array to col
# -note: must be same length!
frame2["debt"]=list(range(10,15))
frame2
  #        year   state  pop  debt
  # one    2000    Ohio  1.5    10
  # two    2001    Ohio  1.7    11
  # three  2002    Ohio  3.6    12
  # four   2001  Nevada  2.4    13
  # five   2002  Nevada  2.9    14
frame2["debt"]=np.arange(5.)
frame2
 #        year   state  pop  debt
 # one    2000    Ohio  1.5     0
 # two    2001    Ohio  1.7     1
 # three  2002    Ohio  3.6     2
 # four   2001  Nevada  2.4     3
 # five   2002  Nevada  2.9     4

# # assigning Series to col
# # -note: matches vals based on
# #        Series index <-> frame2 index
val=pd.Series(
    [-1.2,-1.5,-1.7],
    index=["two","four","five"]
)
frame2["debt"]=val
frame2
 #        year   state  pop  debt
 # one    2000    Ohio  1.5   NaN
 # two    2001    Ohio  1.7  -1.2
 # three  2002    Ohio  3.6   NaN
 # four   2001  Nevada  2.4  -1.5
 # five   2002  Nevada  2.9  -1.7
#
# # assigning new col that DNE creates that new col
frame2["eastern"]=(frame2.state=="Ohio")
frame2
 #        year   state  pop  debt eastern
 # one    2000    Ohio  1.5   NaN    True
 # two    2001    Ohio  1.7  -1.2    True
 # three  2002    Ohio  3.6   NaN    True
 # four   2001  Nevada  2.4  -1.5   False
 # five   2002  Nevada  2.9  -1.7   False
#
 
