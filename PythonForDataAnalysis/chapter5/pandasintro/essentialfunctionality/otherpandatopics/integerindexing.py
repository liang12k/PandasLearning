"""
data selection with integers will always be 
label-orientated (cols' label name)

.iget_value: position-based indexing (Series)

.irow, .icol: (DataFrame)
"""

import numpy as np
from pandas import DataFrame, Series

ser=Series(np.arange(3.)); ser
'''
0    0
1    1
2    2
dtype: float64
'''
# ser[-1] # throws keyerror;
#           ambiguity because of numerical index
ser[-1:]
'''
2    2
dtype: float64
'''
# data selection with integers will always be
# label-orientated
ser.ix[1:2]
'''
1    1
2    2
dtype: float64
'''

ser2=Series(
    np.arange(3.),
    index=list("abd")
)
ser2
'''
a    0
b    1
d    2
dtype: float64
'''
# non-integer index: no ambiguity
ser2[-1]
# 2.0

# # .iget_value: position-based indexing (Series)
# # .irow, .icol: (DataFrame)
ser3=Series(range(3), index=[-5,1,3]); ser3
'''
-5    0
 1    1
 3    2
dtype: int64
'''
ser3.iget_value(2)
# 2

s=Series([4,9,1,3,8,2]); s
'''
0    4
1    9
2    1
3    3
4    8
5    2
dtype: int64
'''
s.iget_value(1); s.iget_value(4); s.iget_value(0)
# 9, 8, 4

frame=DataFrame(
    np.arange(6).reshape(3,2), # 3x2 matrix
    index=[2,0,1]
)
frame
'''
   0  1
2  0  1
0  2  3
1  4  5
'''
frame.irow(0)
# get row 0 (index==2), get values of all its cols
'''
0    0
1    1
Name: 2, dtype: int64
'''
frame.irow(2)
# get row 2 (index==1), get vals of all its cols
'''
0    4
1    5
Name: 1, dtype: int64
'''
frame.icol(1) # in this case, ==frame.icol(-1)
'''
2    1
0    3
1    5
Name: 1, dtype: int64
'''
