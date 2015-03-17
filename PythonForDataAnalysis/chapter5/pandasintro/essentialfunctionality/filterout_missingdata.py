"""
.dropna: return only non-null data, index values
         -default drops rows, cols that are NA

: thresh arg requires that many non-NaN values
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
# per column
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
# per row
'''
    0    1   2
0   1  6.5   3
1   1  NaN NaN
2 NaN  NaN NaN
3 NaN  6.5   3
'''

# # filtering out DataFrame rows with
# # concerns to time series data
df=pd.DataFrame(np.random.randn(7,3))
df
'''
          0         1         2
0  0.169538 -1.596047 -0.150498
1  1.325532  1.162959  0.606870
2  0.804475  0.768876  0.408387
3  1.555792 -0.211204 -1.693698
4 -0.476087  0.568910 -0.625268
5  0.814673  0.768167  1.029957
6  1.277116 -0.697095 -0.134517
'''
df.ix[:4,1]=NA; df.ix[:2,2]=NA; df
# syntax: df.ix[rXi : rXn, [cIdx1,cIdx2,...]]
# replace col 1, rows 0:4 = NA
# replace col 2, rows 0:2 = NA
'''
          0         1         2
0  0.169538       NaN       NaN
1  1.325532       NaN       NaN
2  0.804475       NaN       NaN
3  1.555792       NaN -1.693698
4 -0.476087       NaN -0.625268
5  0.814673  0.768167  1.029957
6  1.277116 -0.697095 -0.134517
'''
# # reminder: if df.ix[:n], get n rows of all cols
df.ix[:3]
'''
          0   1         2
0  0.169538 NaN       NaN
1  1.325532 NaN       NaN
2  0.804475 NaN       NaN
3  1.555792 NaN -1.693698
'''
df.ix[:4,[2,0]]
# get cols order 2,0 and rows 0:4
'''
          2         0
0       NaN  0.169538
1       NaN  1.325532
2       NaN  0.804475
3 -1.693698  1.555792
4 -0.625268 -0.476087
'''
df.dropna()
# drop all rows,cols w NaN value
'''
          0         1         2
5  0.814673  0.768167  1.029957
6  1.277116 -0.697095 -0.134517
'''
# **note: df.dropna(how="all")
#         for either axis 0,1 pointless as
#         not entire rows or cols as NaN
df.dropna(thresh=3)
# thresh arg requires that many non-NaN values
# : requires row w 3 cols w non-NaN values
'''
          0         1         2
5  0.814673  0.768167  1.029957
6  1.277116 -0.697095 -0.134517
'''
df.dropna(thresh=2)
'''
          0         1         2
3  1.555792       NaN -1.693698
4 -0.476087       NaN -0.625268
5  0.814673  0.768167  1.029957
6  1.277116 -0.697095 -0.134517
'''
