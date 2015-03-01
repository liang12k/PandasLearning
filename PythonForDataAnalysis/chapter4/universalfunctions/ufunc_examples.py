"""

"""

import numpy as np

arr=np.arange(10)
# # np.sqrt is a ufunc
# # takes scalar values in ndarray and
# # produces scalar values

#
# # unary ufuncs: np.sqrt, np.exp
# # ^ math operations involving single element

np.sqrt(arr)
# # note: arr is a 1D array
# array(
#     [ 0.        ,  1.        ,  1.41421356,
#       1.73205081,  2.        ,  2.23606798,
#       2.44948974,  2.64575131,  2.82842712,  3.
#     ]
# )

np.exp(arr)
# # note: arr is a 1D array
# array(
#     [  1.00000000e+00,   2.71828183e+00,
#        7.38905610e+00,   2.00855369e+01,
#        5.45981500e+01,   1.48413159e+02,
#        4.03428793e+02,   1.09663316e+03,
#        2.98095799e+03,   8.10308393e+03
#    ])

#
# # binary ufuncs: np.maxinum
# # ^ involving 2 elements
#

x = np.random.randn(8)
y = np.random.randn(8)
# element-wise operation, taking max value
# betw x,y per index
np.maximum(x,y) 

#
# # ufunc returning multiple arrays
# # 
# # ex:
# # np.modf - returns fractal and int
# #           part of floating point array
# # ^ : floating number --(separate)-->
# #     whole number array, decimal array
modfarr=np.array(
    [2.419,-9.2356,-0.015926,50.00053,-1947.95721]
)
np.modf(modfarr)
# # note: the whole number is in 2nd array
# #       remaining decimals (fractals) in 1st array
#
# (
#     array(
#         [  4.19000000e-01,  -2.35600000e-01,
#            -1.59260000e-02, 5.30000000e-04,
#            -9.57210000e-01]),
#     array([    2.,    -9.,
#                -0.,    50.,
#                -1947.])
# )

arr2=modfarr
# array(
#     [  2.41900000e+00,
#        -9.23560000e+00,
#        -1.59260000e-02,
#        5.00005300e+01,
#        -1.94795721e+03]
# )

np.abs(arr2) # absolute value of all vals

np.square(arr2) # == arr**2, square all elements

np.log(arr2) # log on valid values
# array(
#     [ 0.88335423,
#       nan,
#       nan,
#       3.91203361,
#       nan]
# )

np.sign(arr2) # sign of each element (pos=1,zero=0,neg=-1)
# array([ 1., -1., -1.,  1., -1.])

np.ceil(arr2) # get ceil of scalar elements
