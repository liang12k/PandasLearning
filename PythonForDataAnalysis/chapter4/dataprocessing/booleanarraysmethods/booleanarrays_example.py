"""
np.any, np.all similar to python

np.sum : gets count of True values

non-zero values == True
"""

import numpy as np

arr=np.random.randn(100)
(arr>0).sum() # get number of positive values

bools=np.array([False,False,True,False])
bools.any() # True  # 1+ True values amongst 1* False
bools.all() # False # 1+ False values amongst 1* True
