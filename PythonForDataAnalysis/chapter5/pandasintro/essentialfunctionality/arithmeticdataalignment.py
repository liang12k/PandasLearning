"""
arithmetic between objects with different indexes
-note: adding together objects w different index pairs
       will result in union of index pairs
"""

import numpy as np
import pandas as pd
# from string import ascii_lowercase

s1=pd.Series(
    [7.3,-2.5,3.4,1.5],
    # index=[_ for _ in ascii_lowercase[:4]],
    index=["a","c","d","e"]
)
s2=pd.Series(
    [-2.1,3.6,-1.5,4,3.1],
    index=["a","c","e","f","g"]
)
s1
# a    7.3
# c   -2.5
# d    3.4
# e    1.5
# dtype: float64
s2
# a   -2.1
# c    3.6
# e   -1.5
# f    4.0
# g    3.1
# dtype: float64
s1+s2
# a    5.2
# c    1.1
# d    NaN
# e    0.0
# f    NaN
# g    NaN
# dtype: float64

# # 
