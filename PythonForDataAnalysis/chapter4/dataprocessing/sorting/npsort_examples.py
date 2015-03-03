"""
sorting: in-place

http://docs.scipy.org/doc/numpy/reference/generated/numpy.sort.html

np.sort(a, axis=-1, kind='quicksort', order=None)
: a = array
  axis = (0:cols),(1:rows),(-1:last axis)
  kind = {‘quicksort’, ‘mergesort’, ‘heapsort’}
  order = list of what to order by (~schema, dtypes)
"""

import numpy as np

arr=np.random.randn(8)
# # ex. arr as randn is different for each creation
arr
# array([
#     0.45543193,  1.37876451, -0.97366233,
#     1.85555894,  0.98138543, 1.74303487,
#     1.03155817,  0.36935903
# ])
arr.sort()
# array([
#     -0.97366233, 0.36935903,  0.45543193,
#     0.98138543,  1.03155817,  1.37876451,
#     1.74303487,  1.85555894
# ])

# # multi-dimensional arrays
# # -can each have 1D section of values
# # sorted in-place based on axis number
# # 0==col, 1==rows, -1==last axis
#
arr=np.random.randn(5,3)
# # ex. randn array
# array([
#     [ 0.20932814,  1.12678365, -1.65196317],
#     [ 0.54360136,  1.31270527,  0.35580245],
#     [ 0.13294224,  0.6284479 , -1.4272088 ],
#     [ 0.48554642,  0.33946776,  0.17408735],
#     [ 0.88415954, -0.76071314, -1.05023642]
# ])
arr.sort(1) # by rows
# array([
#     [-1.65196317,  0.20932814,  1.12678365],
#     [ 0.35580245,  0.54360136,  1.31270527],
#     [-1.4272088 ,  0.13294224,  0.6284479 ],
#     [ 0.17408735,  0.33946776,  0.48554642],
#     [-1.05023642, -0.76071314,  0.88415954]
# ])
#
#
# # note: this is .sort(0) based on the
# #       above arr.sort(1) output as .sort
# #       operates in-place
#
arr.sort(0)
# array([
#     [-1.65196317, -0.76071314,  0.48554642],
#     [-1.4272088 ,  0.13294224,  0.6284479 ],
#     [-1.05023642,  0.20932814,  0.88415954],
#     [ 0.17408735,  0.33946776,  1.12678365],
#     [ 0.35580245,  0.54360136,  1.31270527]
# ])

# # top level np.sort returns sorted copy of an
# # array instead of in-place array modifying
# #
# # quick-&-dirty quantile computation
# # -sort then select value at specific rank
# # -note: z (normal) distribution is sorted data
large_arr=np.random.randn(1000)
large_arr.sort() # large_array is 1D
large_arr[int(0.05*len(large_arr))] # 5% quantile
