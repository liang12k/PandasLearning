"""
fancy indexing: indexing using int arrays
"""

import numpy as np

# np.empty(shape, dtype=float, order='C')
# : shape : int or tuple of int, array .shape
arr = np.empty((8,4))

for i in range(8): arr[i] = i
# arr
# array([
#     [ 0.,  0.,  0.,  0.],
#     [ 1.,  1.,  1.,  1.],
#     [ 2.,  2.,  2.,  2.],
#     [ 3.,  3.,  3.,  3.],
#     [ 4.,  4.,  4.,  4.],
#     [ 5.,  5.,  5.,  5.],
#     [ 6.,  6.,  6.,  6.],
#     [ 7.,  7.,  7.,  7.]
# ])

# getting specific rows in order,
# pass in list, ndarray of ints
# positive ints start from beginning
# negative ints start from end
#
arr[[4,3,0,6]]
# array([
#     [ 4.,  4.,  4.,  4.],
#     [ 3.,  3.,  3.,  3.],
#     [ 0.,  0.,  0.,  0.],
#     [ 6.,  6.,  6.,  6.]
#])
#
arr[[-3,-5,-7]]
# array([
#     [ 5.,  5.,  5.,  5.],
#     [ 3.,  3.,  3.,  3.],
#     [ 1.,  1.,  1.,  1.]
# ])

#
# # passing multiple index arrays
# # selects 1D array of elems corresponding
# # to each tuple of indices
#
# set up array w 32 elems, .reshape to 8x4 array
arr = np.arange(32).reshape((8,4))
# array([
#     [ 0,  1,  2,  3],
#     [ 4,  5,  6,  7],
#     [ 8,  9, 10, 11],
#     [12, 13, 14, 15],
#     [16, 17, 18, 19],
#     [20, 21, 22, 23],
#     [24, 25, 26, 27],
#     [28, 29, 30, 31]
# ])

# this 1st gets row indices [1,5,7,2],
# then 2nd gets col indices (idx position) [0,3,1,2]
# of row indices (1st)
#
# think of it pairing (row, col) idx tuples
# [(1, 0), (5, 3), (7, 1), (2, 2)]
arr[
    [1,5,7,2], # 1st: get row indices of 'arr'
    [0,3,1,2]  # 2nd: get indices of 1st
]
# array([ 4, 23, 29, 10])

# 1st taking row indicies [1,5,7,2]
# 2nd get everything ':' from 1st then
# 3rd get col indices (idx positions) [0,3,1,2]
# and display idx in that order
arr[[1,5,7,2]][:,[0,3,1,2]]
#
# 1st: [[1,5,7,2]]
# ----
# arr[[1,5,7,2]]
# array([
#     [ 4,  5,  6,  7],
#     [20, 21, 22, 23],
#     [28, 29, 30, 31],
#     [ 8,  9, 10, 11]
# ])
#
# 2nd: [:]
# ----
# arr[[1,5,7,2]][:]
# # note the order of elems
# array([
#     [ 4,  5,  6,  7],
#     [20, 21, 22, 23],
#     [28, 29, 30, 31],
#     [ 8,  9, 10, 11]
# ])
#
# 3rd: [:, [0,3,1,2]]
# ----
# arr[[1,5,7,2]][:,[0,3,1,2]]
# # new order and original order (2nd) to the right
# array([
#     [ 4,  7,  5,  6], # [ 4,  5,  6,  7],
#     [20, 23, 21, 22], # [20, 21, 22, 23],
#     [28, 31, 29, 30], # [28, 29, 30, 31],
#     [ 8, 11,  9, 10]  # [ 8,  9, 10, 11]
# ])

# # np.ix_ method converts two 1D int arrays
# # to an indexer that selects square region
# # aka: doing arr[[1,5,7,2]][:,[0,3,1,2]] easier
# 
# arr[np.ix_([1,5,7,2],[0,3,1,2])] == arr[[1,5,7,2]][:,[0,3,1,2]]
# array([
#     [ True,  True,  True,  True],
#     [ True,  True,  True,  True],
#     [ True,  True,  True,  True],
#     [ True,  True,  True,  True]],
# dtype=bool)
#
arr[np.ix_([1,5,7,2],[0,3,1,2])]
# array([
#     [ 4,  7,  5,  6],
#     [20, 23, 21, 22],
#     [28, 31, 29, 30],
#     [ 8, 11,  9, 10]
# ])
