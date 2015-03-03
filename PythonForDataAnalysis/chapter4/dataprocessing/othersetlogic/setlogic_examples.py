"""

"""

import numpy as np

names=np.array(
    ["Bob","Joe","Will","Bob","Will","Joe","Joe"]
)
np.unique(names)
# array(['Bob', 'Joe', 'Will'], dtype='|S4')

ints=np.array([3,3,3,2,2,1,1,4,4])
np.unique(ints)
# array([1, 2, 3, 4])

# also get indices of 1st occurrence of element
np.unique(ints, return_index=True)
# (array([1, 2, 3, 4]), array([5, 3, 0, 7]))

# # np.in1d: arrays values of x1 in x2; bools return
values=np.array([6,0,0,3,2,5,6])
np.in1d(values,[2,3,6])
# array([ True, False, False,  True,
#         True, False,  True], dtype=bool)
#
# for inversion: np.ind1d(x1,x2,invert=True)

# # 
# # np set methods
# #
np.unique      # sorted, unique elements of x1
np.intersect1d # sorted, common elements in x1,x2
np.union1d     # sorted, union of elements of x1,x2
np.in1d        # bool array of x1 elements in x2
np.setdiff1d # set difference, x1 elements not in x2
np.setxof1d  # symmetric difference,
             # elements in either x1,x2 BUT not both!
             # XOR: element meets 1 cond, not both
