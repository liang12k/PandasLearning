"""
ndarray : N-dimensional array obj
-fast, flexible container for large data sets in Python
-container for homogenous data (all elems are same type)

arrays: perform mathematical operations on whole blocks
of data using similar syntax to equivalent operations 
between scalar elements

scalar: simple numbers for measuring things
"""

import numpy as np

data = np.array([
    [0.9256,-0.246,-0.8856],
    [0.5639,2.3794,9.104]
])

# data * 10
# array([[  9.256,  -2.46 ,  -8.856],
#       [  5.639,  23.794,  91.04 ]])

# data + data
# array([[  1.8512,  -0.492 ,  -1.7712],
#       [  1.1278,   4.7588,  18.208 ]])

# data.shape # (2,3) # indicating rows, cols

# data.dtype # dtype('float64')

# #
# # creating ndarrays
# # 

data1 = [6,7.5,8,0,1]
arr1 = np.array(data1)
# arr1 # array([ 6. ,  7.5,  8. ,  0. ,  1. ])
# arr1.dtype # dtype('float64')

data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2)
# arr2 # array([[1, 2, 3, 4],[5, 6, 7, 8]])
# arr2.ndim # array dimensions, num of axes # 2
# arr2.shape # array shape # (2, 4)
# arr2.dtype # dtype('int64')

# #
# # create an array of zeros
# # 
zeros1 = np.zeros(10)
# array([ 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

zeros2 = np.zeros((3,6))
# array([[ 0.,  0.,  0.,  0.,  0.,  0.],
#       [ 0.,  0.,  0.,  0.,  0.,  0.],
#       [ 0.,  0.,  0.,  0.,  0.,  0.]])
zeros2.shape
# (3, 6)

# # .empty: return a new array of given shape and type,
# # without initializing entries
# # -may return uninitialized garbage values
empty1 = np.empty((2,3,2))
# array([
#     [
#         [ -1.72723371e-077,  -1.72723371e-077],
#         [  2.13779680e-314,   1.75871011e-310],
#         [ -1.72723371e-077,  -1.72723371e-077]
#     ],
# 
#     [
#         [  2.13786155e-314,   2.14522316e-314],
#         [  2.15963495e-314,   2.15963533e-314],
#         [  2.13856065e-314,   2.15963540e-314]
#     ]
# ])
# empty1.shape # (2, 3, 2)
# empty1.ndim # 3 # 3 axes

arange1 = np.arange(15)
# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])


