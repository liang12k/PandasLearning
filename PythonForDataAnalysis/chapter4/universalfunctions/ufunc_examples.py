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
# # ex: np.modf 
