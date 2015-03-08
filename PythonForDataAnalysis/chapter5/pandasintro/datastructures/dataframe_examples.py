"""
DataFrame: tabular, spreadsheet-like data structure
           containing ordered collection of cols
           ^ each col can be diff val (~qztable.Schema)
           has row,col index
           kind of dict of Series (sharing same idx)
           ** data stored as 1D or 2D blocks

-note: cols returned when indexing is a view on
       dataframe, not a copy.
       in-place modifications to Series reflected in
       the dataframe. 
       Series.copy method explicitly copies Series
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
# # deleting cols
del frame2["eastern"]
frame2
 #        year   state  pop  debt
 # one    2000    Ohio  1.5   NaN
 # two    2001    Ohio  1.7  -1.2
 # three  2002    Ohio  3.6   NaN
 # four   2001  Nevada  2.4  -1.5
 # five   2002  Nevada  2.9  -1.7
#
# # deleting multiple cols using .drop
# # -in place deletion and on rows
# #  http://stackoverflow.com/questions/13411544/delete-column-from-pandas-dataframe
# frame2.drop(["state","debt"],inplace=True,axis=1)
# frame2
 #        year  pop
 # one    2000  1.5
 # two    2001  1.7
 # three  2002  3.6
 # four   2001  2.4
 # five   2002  2.9
#

# # creating dataframe from nested dicts
# # -keys are indices
pop={
    "Nevada":{
        2001:2.4,
        2002:2.9
    },
    "Ohio":{
        2000:1.5,
        2001:1.7,
        2002:3.6
    },
}
frame3=pd.DataFrame(pop)
frame3.index.name="year"
frame3
 #       Nevada  Ohio
 # year
 # 2000     NaN   1.5
 # 2001     2.4   1.7
 # 2002     2.9   3.6
#
# # transpose dataframe
frame3.T
# year    2000  2001  2002
# Nevada   NaN   2.4   2.9
# Ohio     1.5   1.7   3.6
#

# # dict of series treated same way as nested dicts
pdata={
    "Ohio":frame3["Ohio"][:-1],
    "Nevada":frame3["Nevada"][:2]
}
pd.DataFrame(pdata)
 #       Nevada  Ohio
 # year
 # 2000     NaN   1.5
 # 2001     2.4   1.7
#
# # setting in dataframe index,cols names
frame3.index.name="year"
frame3.columns.name="state"
frame3
# state  Nevada  Ohio
# year
# 2000      NaN   1.5
# 2001      2.4   1.7
# 2002      2.9   3.6
frame3.T
# year    2000  2001  2002
# state
# Nevada   NaN   2.4   2.9
# Ohio     1.5   1.7   3.6
#
# # dataframe.values returns dataframe's data
# # as 2D ndarray
frame3.values
# array([
#     [ nan,  1.5],
#     [ 2.4,  1.7],
#     [ 2.9,  3.6]
# ])
#
# # different dtypes in dataframe's cols
# # dtype of the .values array will be
# # chosen to accomdate all the cols
frame2
 #         year   state  pop  debt
 # one     2000    Ohio  1.5   NaN
 # two     2001    Ohio  1.7  -1.2
 # three   2002    Ohio  3.6   NaN
 # four    2001  Nevada  2.4  -1.5
 # five    2002  Nevada  2.9  -1.7
frame2.values
# array([
#     [2000, 'Ohio', 1.5, nan],
#     [2001, 'Ohio', 1.7, -1.2],
#     [2002, 'Ohio', 3.6, nan],
#     [2001, 'Nevada', 2.4, -1.5],
#     [2002, 'Nevada', 2.9, -1.7]
# ],dtype=object)
#

# # Table 5-1
# # some wrangling on the table's text to
# # put it into a dataframe
#
{'Chapter5_Table5-4':{'2D ndarray': 'A matrix of data, passing optional row and column labels',
                       'Another DataFrame': "The DataFrame's indexes are used unless different ones are passed",
                       'List of lists or tuples': "Treated as the '2D ndarray' case",
                       'NumPy MaskedArray': "Like the '2D ndarray' case except masked values become NA/missing in the DataFrame result",
                       'NumPy structured/record array': "Treated as the 'dict of arrays' case",
                       'array dict of Series': "Each value becomes a column. Indexes from each Series are unioned together to form the result's row index if no explicit index is passed.",
                       'dict of arrays, lists, or tuples': 'Each sequence becomes a column in the DataFrame. All sequences must be the same length.',
                       'dict of dicts': "Each inner dict becomes a column. Keys are unioned to form the row index as in the 'dict of Series' case.",
                       'list of dicts or Series': "Each item becomes a row in the DataFrame. Union of dict keys or Series indexes become the DataFrame's column labels"}}
