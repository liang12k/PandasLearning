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
