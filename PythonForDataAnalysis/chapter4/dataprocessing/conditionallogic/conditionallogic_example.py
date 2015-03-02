"""

"""

import numpy as np

# [start,end)
xarr=np.arange(1.1,1.6,0.1)
yarr=np.arange(2.1,2.6,0.1)
cond=np.array([True,False,True,True,False])

#
# # **PROBLEMS**
# # ------------
# # with the for-loop:
# # 1. slow for large arrays
# # 2. won't work with multi-dimensional arrays
#
result = [(x if c else y)
          for x,y,c in zip(xarr,yarr,cond)]
#  [1.1000000000000001,
#   2.2000000000000002,
#   1.3000000000000003,
#   1.4000000000000004,
#   2.5000000000000004]

#
# # **SOLUTION**
# # np.where : True yields x1, False yields x2
# # -note: x1,x2 don't need to be arays
# #        either/both can be scalars
result = np.where(cond, xarr, yarr)
# array([ 1.1,  2.2,  1.3,  1.4,  2.5])

# rand (4,4) array
arr=randn(4,4)
# all vals > 0 output 2, else -2
np.where(arr>0,2,-2)
# all vals > 0 output 2, else the elem as-is
np.where(arr>0,2,arr)

# # streamlining numerous if-elif-else statement
# # using np.where, one-liner sytax
#
# 'pythonic' for-loop nested syntax
# result=[]
# for i in range(n):
#     if cond1[i] and cond2[i]: result.append(0)
#     elif cond1[i]: result.append(1)
#     elif cond2[i]: result.append(2)
#     else: result.append(3)
# 
# into nested np.where
# -the arg using nested np.where
# result = [
#     np.where(
#         cond1 and cond2, 0,
#             np.where(cond1, 1,
#                      np.where(cond2, 2, 3))
# )]

# 'cryptic' syntax
# result = 1*cond1 + 2*cond2 + 3*-(cond1|cond2)
