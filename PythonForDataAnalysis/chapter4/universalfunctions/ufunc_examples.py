1"""

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
              # the smallest int value >= element
# array([    3.,    -9.,    -0.,    51., -1947.]

np.floor(arr2) # get floor of scalar elements
               # the largest int value <= element
# array(
#      [ 2.00000000e+00,
#        -1.00000000e+01,
#        -1.00000000e+00,
#        5.00000000e+01,
#        -1.94800000e+03]
# )

np.rint(arr2) # round elements to nearest int,
              # perserving dtype
# array([    2.,    -9.,    -0.,    50., -1948.])

np.isnan(arr2) # get bool array indicating each
               # value == NaN (not-a-number)

np.isfinite # each element is finite (non-inf, non-NaA)
np.isinf # each element is infinite

# trigonometric functions & hyperbolic alternative
# inverse trigonometric functions
np.cos, np.cosh, np.arccos, np.arccosh
np.sin, np.sinh, np.arcsin, np.arcsinh
np.tan, np.tanh, np.arctan, np.arctanh

# logic applied to elements
np.logical_and, np.logical_or, np.logical_not
np.logical_xor # element satisfy ONLY one of critera
               # arr1, arr2 must be same shape
# ^ http://goo.gl/0k8lF2
# Joe==male,25, Bob==male,30, Anne==female,25
# "male AND 25"==Joe
# "male OR 25"==Joe,Bob,Anne (**OR condition)
# "male XOR 25"==Bob,Anne (only meet 1 condition)

# 
# # binary ufunc
#
np.add # add corresponding elements in x1,x2 arrays
np.subtract # '' similar, subtrace
np.multiply # '' similar, multiple
np.divide   # '' similar, divide
np.floor_divide # '' similar, remove remainder

np.power # x1 array elements raised to x2 values
         # x2's values are x1 elements' exponents
# np.power(np.arange(4),np.array([5,3,4,2]))
# array([ 0,  1, 16,  9]) # [0^5, 1^3, 2^4, 3^2]

np.maximum # output array w max vals of
           # each index from each array
np.minimum # '' similar, minimum
np.fmax    # similar to np.maximum, ignore NaN vals
np.fmin    # similar to np.minimum, min

np.mod     # '' similar, mod operation
np.copysign# '' similar, copy sign of x2 into x1

# # greater, less, equal assorted
# # x2 values compared to x1 values
np.greater, np.greater_equal
np.less,    np.less_equal
np.equal,   np.not_equal

