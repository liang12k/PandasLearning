"""
getting a subset of data, individual elements

slice: selects a range of elems along an axis

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
# # commenting out to avoid affecting rest of exercises
# arr = np.arange(10)
# arr_slice = arr[5:8].copy()
# arr_slice[1] = 12345
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

# old_values
# array([[1, 2, 3],
#        [4, 5, 6]])

arr3d[0] = old_values
# arr3d
# array([[[ 1,  2,  3],
#         [ 4,  5,  6]],
#        [[ 7,  8,  9],
#         [10, 11, 12]]])

# arr3d[1,0] == arr3d[1][0] # array([7, 8, 9])

# # indexing with slices
# arr[1:6] # array([ 1,  2,  3,  4, 64])

# arr2
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])
# 
# arr2[:2] # reminder: arr2 was a 3x3 array
# array([[1, 2, 3],
#        [4, 5, 6]])

# arr2d[:2,:1]
# array([[1],
#        [4]])
# 
# arr2d[:2,1:]
# array([[2, 3],
#        [5, 6]])

# # slicing by mixing int indexes and slices
# # receive lower dimensional slices
# arr2d[1,:2] # array([4, 5])
# arr2d[2,:1] # array([7])
# 
# arr2d[:,:1] # ':' represents taking the whole axis
# array([[1],
#        [4],
#        [7]])

arr2d[:2,:1] = 0 # assigning to entire slice area
# arr2d
# array([[0, 2, 3],
#        [0, 5, 6],
#        [7, 8, 9]])
