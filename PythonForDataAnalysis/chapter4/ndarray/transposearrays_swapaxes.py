"""
transposing: reshaping, return view on data w/o copying
: .T attribute
"""

import numpy as np

arr=np.arange(15).reshape((3,5))
# arr
# array([
#     [ 0,  1,  2,  3,  4],
#     [ 5,  6,  7,  8,  9],
#     [10, 11, 12, 13, 14]
# ])

# # transpose 3x5 to 5x3
# arr.T
# array([
#     [ 0,  5, 10],
#     [ 1,  6, 11],
#     [ 2,  7, 12],
#     [ 3,  8, 13],
#     [ 4,  9, 14]
# ])

# # matrix computations using transpose
# ref: http://mathinsight.org/dot_product_matrix_notation
# 
# ex: (X^T)X using np.dot
# np.dot(arr.T, arr)
# array([
#     [125, 140, 155, 170, 185],
#     [140, 158, 176, 194, 212],
#     [155, 176, 197, 218, 239],
#     [170, 194, 218, 242, 266],
#     [185, 212, 239, 266, 293]
# ])

# # higher dimensional arrays
# # transpose will take tuple of axis numbers
# # to permute axes
#
# create array of 16 elems: (2,2,4) .shape
# 2 sub-ndarrays
# : ^ 2 ndarrays in each sub-ndarray
# :   ^ 4 elems in each ndarray
#
arr=np.arange(16).reshape((2,2,4))
# array([
#     [[ 0,  1,  2,  3],
#      [ 4,  5,  6,  7]],
#     [[ 8,  9, 10, 11],
#      [12, 13, 14, 15]]
# ])
arr.transpose((1,0,2))
# array([
#     [[ 0,  1,  2,  3],
#      [ 8,  9, 10, 11]],
#     [[ 4,  5,  6,  7],
#      [12, 13, 14, 15]]
# ])
arr.shape # (2,2,4)
# these are the orig arr axes' indices:
# i0=2,i1=2,i2=4
# 
arr.transpose((1,0,2))
# transpose by: i0 --> i1, i1 --> i0, i2
# shape is still: (2,2,4)
arr.transpose((2,0,1))
# transpose by: i0 --> i2, i1 --> i0, i2 --> i1
# shape is now: (4,2,2)
arr.transpose((1,2,0))
# transpose by: i0 --> i1, i1 --> i2, i2 --> i0
# shape is now: (2,4,2)

# ----
# create array of 16 elems: (2,4,2) .shape
# 2 sub-ndarrays
# : ^ 4 ndarrays in each sub-ndarray
# :   ^ 2 elems in each ndarray
# np.arange(16).reshape((2,4,2))

# # .swapaxes: returns view on data w/o making a copy
arr.swapaxes(1,2)
# array([
#     [[ 0,  4],
#      [ 1,  5],
#      [ 2,  6],
#      [ 3,  7]],
#     [[ 8, 12],
#      [ 9, 13],
#      [10, 14],
#      [11, 15]]
# ])
