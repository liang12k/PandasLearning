"""
getting a subset of data, individual elements

slices on arrays are views on original array
: any changes done on view --> changes original array
: ^ think mutability of lists**
: to perserve original (make copy of slice)
: # ndarray[i0:iN].copy()
"""

import numpy as np

# 1D arrays == lists
arr = np.arange(10)
# arr[5] # 5
# arr[5:8] # array([5, 6, 7])
# # assigning indexes [5-7] with 12
# # value is propagated (broadcasted)
# arr[5:8] = 12; arr # array([ 0,  1,  2,  3,  4, 12, 12, 12,  8,  9])

arr_slice = arr[5:8]
# this change applies to arr[6] since [1] idx of [5:8]
arr_slice[1] = 12345
# arr # array([    0,     1,     2,     3,     4,     5, 12345,     7,     8,     9])
# this change applies to whole arr[5:8]
arr_slice[:] = 64
# arr # array([ 0,  1,  2,  3,  4, 64, 64, 64,  8,  9]

# # trying out the ndarray.copy for slicing
arr = np.arange(10)
arr_slice = arr[5:8].copy()
arr_slice[1] = 12345
# arr_slice # array([    5, 12345,     7])
# arr # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


