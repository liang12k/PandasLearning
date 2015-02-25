"""
dtype: data type is a special obj containing info the
       ndarray needs to interpret chunk of memory as 
       a particular type of data
       ** homegenous throughout np.array

syntax format: 
<typename><bytes> # bytes = bits per element
ex: int64, float32

astype: converting array dtype to new dtype
        ** this always creates a new array (copy of data)

"""

import numpy as np

# explicitly casting array from one dtype to another
arr1 = np.arange(5)
# arr1.dtype # dtype('int64')

float_arr1 = arr.astype(np.float64)
# float_arr1.dtype # dtype('float64')

arr2 = np.array([3.7,-1.2,-2.6,0.5,12.9,10.1])
# arr2.dtype # dtype('float64')
# arr2.astype(np.int32) # array([ 3, -1, -2,  0, 12, 10], dtype=int32)

numeric_strings1 = np.array(
    ["1.25","-9.6","42"], dtype=np.string_
)
# # **Note: casting as float (same as np.float)
# numeric_strings1.astype(float) # array([  1.25,  -9.6 ,  42.  ])

# # using another array's dtype for converting
int_array = np.arange(10)
calibers = np.array(
    [.22,.270,.357,.380,.44,.50],
    dtype=np.float64
)
# int_array.astype(calibers.dtype)
# array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.])


