"""
.sort_index: sorting data set by criterion
-lexicographically by row or col index
 (^: alphabetical order of components, dict order)

-**note: returns new sorted object

pd.Series : .sort_index, .sort
pd.DataFrame : .sort_index(axis=num,ascending=bool)

.rank: data ranking with ties being assigned 
       the mean of the ranks for the group
       -**note: NaN are excluded
       -http://en.wikipedia.org/wiki/Ranking#Ranking_in_statistics
       -http://pandas.pydata.org/pandas-docs/dev/computation.html#data-ranking
"""

import numpy as np
import pandas as pd

obj=pd.Series(
    range(4),
    index=list("dabc")
)
obj
# d    0
# a    1
# b    2
# c    3
# dtype: int64
obj.sort_index()
# a    1
# b    2
# c    3
# d    0
# dtype: int64
frame=pd.DataFrame(
    np.arange(8).reshape((2,4)),
    index=["three","one"],
    columns=list("dabc")
)
frame
#        d  a  b  c
# three  0  1  2  3
# one    4  5  6  7
frame.sort_index()
#        d  a  b  c
# one    4  5  6  7
# three  0  1  2  3
#
# sort order by col then by its cell value
frame.sort_index(axis=1,ascending=False)
#        d  c  b  a
# three  0  3  2  1
# one    4  7  6  5

# # Series values sort using .order
obj=pd.Series([4,7,-3,2])
obj
# 0    4
# 1    7
# 2   -3
# 3    2
# dtype: int64
obj.order()
# 2   -3
# 3    2
# 0    4
# 1    7
# dtype: int64
obj=pd.Series([4,np.nan,7,np.nan,-3,2])
obj
# 0     4
# 1   NaN
# 2     7
# 3   NaN
# 4    -3
# 5     2
# dtype: float64
obj.order()
# 4    -3
# 5     2
# 0     4
# 2     7
# 1   NaN
# 3   NaN
# dtype: float64
frame=pd.DataFrame(
    {
        "b":[4,7,-3,2],
        "a":[0,1,0,1]
    }
)
frame
#    a  b
# 0  0  4
# 1  1  7
# 2  0 -3
# 3  1  2
frame.sort_index(by="b")
#    a  b
# 2  0 -3
# 3  1  2
# 0  0  4
# 1  1  7
frame.sort_index(by="a")
#    a  b
# 0  0  4
# 2  0 -3
# 1  1  7
# 3  1  2
frame.sort_index(by=["a","b"])
#    a  b
# 2  0 -3
# 0  0  4
# 3  1  2
# 1  1  7

# # ranking
obj=pd.Series([7,-5,7,4,2,0,4])
obj
# 0    7
# 1   -5
# 2    7
# 3    4
# 4    2
# 5    0
# 6    4
# dtype: int64
obj.rank()
# .rank of tied values uses the mean
#
# 0    6.5
# 1    1.0
# 2    6.5
# 3    4.5
# 4    3.0
# 5    2.0
# 6    4.5
# dtype: float64
obj.rank(method="first")
# ranking method - taking whole int
# 
# 0    6
# 1    1
# 2    7
# 3    4
# 4    3
# 5    2
# 6    5
# dtype: float64
obj.rank(ascending=False,method="max")
# 0    2
# 1    7
# 2    2
# 3    4
# 4    5
# 5    6
# 6    4
# dtype: float64
obj.rank(ascending=True,method="first")
# rank by 'first' occurrence of indices
#
# 0    6
# 1    1
# 2    7
# 3    4
# 4    3
# 5    2
# 6    5
# dtype: float64
frame=pd.DataFrame(
    {
        "b":[4.3,7,-3,2],
        "a":[0,1,0,1],
        "c":[-2,5,8,-2.5]
    }
)
frame
#    a    b    c
# 0  0  4.3 -2.0
# 1  1  7.0  5.0
# 2  0 -3.0  8.0
# 3  1  2.0 -2.5
frame.rank(axis=1)
# rank based on rows
#
#    a  b  c
# 0  2  3  1
# 1  1  3  2
# 2  2  1  3
# 3  2  3  1

# # Table5-8: breaking methods with rank
{"'average'": 'Default: assign the average rank to each entry in the equal group.',
 "'first'": 'Assign ranks in the order the values appear in the data.',
 "'max'": 'Use the maximum rank for the whole group.',
 "min'": 'Use the minimum rank for the whole group.'}
