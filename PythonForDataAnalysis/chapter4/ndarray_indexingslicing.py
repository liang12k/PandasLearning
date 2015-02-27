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

# # 2D array
arr2d = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
# arr2d[2] # array([7, 8, 9])
# arr2d[0][2] == arr2d[0,2] # 3

# # multi-dimensional arrays
# 2x2x3 array
arr3d = np.array([
    [[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]]
])
# arr3d.shape # (2, 2, 3)
# arr3d
# array([[[ 1,  2,  3],
#         [ 4,  5,  6]],
#        [[ 7,  8,  9],
#         [10, 11, 12]]])

# arr3d
# array([[1, 2, 3],
#        [4, 5, 6]])
# arr3d.shape # (2, 3)

# assigning scalar, arrays to arr3d[idx]
old_values = arr3d[0].copy() # keep orig arr3d
arr3d[0] = 42
# array([[[42, 42, 42],
#         [42, 42, 42]],
#        [[ 7,  8,  9],
#         [10, 11, 12]]])

