"""
numpy.concatenate:
-data combination with raw numpy arrays
"""

import numpy as np
import pandas as pd

arr=np.arange(12).reshape((3,4))
print arr
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''
print np.concatenate([arr,arr],axis=1)
'''
[[ 0  1  2  3  0  1  2  3]
 [ 4  5  6  7  4  5  6  7]
 [ 8  9 10 11  8  9 10 11]]
'''
