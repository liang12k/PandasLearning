"""
reductions (aka aggregations):
-called with array instance or np function

normal distribution (aka probability distribution)
-"Gaussian distribution"
>http://simple.wikipedia.org/wiki/Normal_distribution
: mean==location, std==scale
-best for large data population

standard normal distribution (aka z distribution)
-normal distribution w mean==0, variance==1
-bell curve design

axis:
-----
 0  = col
 1  = row
 ...
 -1 = last axes (in a 2D array, it would be 'y' (col)

 when axis not given, calculate over flattened array
"""

import numpy as np

arr=np.random.randn(5,4) # normal-distributed data
arr.mean() # == np.mean(arr)
arr.sum()
# can do individual row opers: arr[row_idx].sum()

# # non-aggregating methods:
# # ex: cumsum, cumprod
arr=np.arange(0,9).reshape((3,3))
# same as:
# np.array([
#     [0,1,2],
#     [3,4,5],
#     [6,7,8]
# ])
#
# # cumsum: a, a+b, a+b+c, a+b+c+d, ...
arr.cumsum(0)  # col
# array([
#     [ 0,  1,  2],
#     [ 3,  5,  7],
#     [ 9, 12, 15]
# ])
arr.cumsum(1) # row
# array([
#     [ 0,  1,  3],
#     [ 3,  7, 12],
#     [ 6, 13, 21]
# ])
#
arr.cumprod(0) # col
# array([
#     [ 0,  1,  2],
#     [ 0,  4, 10],
#     [ 0, 28, 80]
# ])
arr.cumprod(1) # row
# array([
#     [  0,   0,   0],
#     [  3,  12,  60],
#     [  6,  42, 336]
# ])
#

arr.argmin() # gets index of min element
arr.argmax() # '' similar, max

# # standard deviation:
# measurement of group spread out from average
# high std == spread out from average
# low std  == close to average
arr.std()

# # variance:
# measurement of how far set of numbers spread out
arr.var()


