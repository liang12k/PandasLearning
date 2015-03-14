"""
.sort_index: sorting data set by criterion
-lexicographically by row or col index
 (^: alphabetical order of components, dict order)

-**note: returns new sorted object

pd.Series : .sort_index, .sort
pd.DataFrame : .sort_index(axis=num,ascending=bool)

.rank: ranking - 
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
