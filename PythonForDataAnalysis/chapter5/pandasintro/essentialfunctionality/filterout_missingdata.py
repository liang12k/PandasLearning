"""
.dropna: return only non-null data, index values
         -default drops rows, cols that are NA
"""

import numpy as np
from numpy import nan as NA
import pandas as pd

data=pd.Series([1,NA,3.5,NA,7])
data
# 0    1.0
# 1    NaN
# 2    3.5
# 3    NaN
# 4    7.0
# dtype: float64
data.dropna()
# == data[data.notnull()] using bool indexing
#
# 0    1.0
# 2    3.5
# 4    7.0
# dtype: float64

data=pd.DataFrame(
    [[1.,6.5,3.],
     [1.,NA,NA],
     [NA,NA,NA],
     [NA,6.5,3.]]
)
data
'''
    0    1   2
0   1  6.5   3
1   1  NaN NaN
2 NaN  NaN NaN
3 NaN  6.5   3
'''
data.dropna()
# drops all NaN values in row,cols
'''
   0    1  2
0  1  6.5  3
'''
data.dropna(how="all")
# axis=0 default,
# drops only entire rows that are NaN
'''
    0    1   2
0   1  6.5   3
1   1  NaN NaN
3 NaN  6.5   3
'''
data[4]=NA;data # create entire col '4' is NaN
'''
    0    1   2   4
0   1  6.5   3 NaN
1   1  NaN NaN NaN
2 NaN  NaN NaN NaN
3 NaN  6.5   3 NaN
'''
data.dropna(axis=1,how="all")
# axis=1,
# drop entire cols that are NaN (col 4)
'''
    0    1   2
0   1  6.5   3
1   1  NaN NaN
2 NaN  NaN NaN
3 NaN  6.5   3
'''
