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

