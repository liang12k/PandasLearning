"""
vectorization: batch operations on data w/o for-loops
               arithmetic operations betw equal sized
               arrays applies operation element wise

broadcasting: operations betw diff sized arrays (ch12)
"""

import numpy as np

# the book places a dot after the number elements
# using dtype arg to create array as float
arr = np.array(
    [[1,2,3],
     [4,5,6]],
    dtype=float
)

# arr * arr
# array([
#     [  1.,   4.,   9.],
#     [ 16.,  25.,  36.]
# ])

# 1 / arr
# array([
#     [ 1.        ,  0.5       ,  0.33333333],
#     [ 0.25      ,  0.2       ,  0.16666667]
# ])

# arr ** 0.5 # sq.root
# array([
#     [ 1.        ,  1.41421356,  1.73205081],
#     [ 2.        ,  2.23606798,  2.44948974]
# ])
