"""
'and','or' don't work with bool arrays
: use '&', '|'
"""

import numpy as np

names = np.array(
    ["Bob","Joe","Will","Bob","Will","Joe","Joe"]
)
# names.dtype # dtype('S4') # longest string length

# generate array w rand nums, rows=7,cols=4
data = np.random.randn(7,4)

# names == "Bob" # applies bool on all elems
# array([ True, False, False,  True, False, False, False], dtype=bool)

# # Note: to apply the bool onto another array
# #       be sure arrays are same length

# taking the bool indices,
# each True ==> each data row in output
data[names=="Bob"]
# taking all output rows, output idx [2:]
data[names=="Bob",2:]

# not "Bob"
# names != "Bob" == -(names=="Bob")
# array([False,  True,  True, False,  True,  True,  True], dtype=bool)
data[-(names=="Bob")] # == data[names!="Bob"]

# # selecting multiple bools
mask = (names=="Bob") | (names=="Will")
# # Note: '|', not 'or' keywd; 'and','or' don't work with bool arrays
# array([ True, False,  True,  True,  True, False, False], dtype=bool)
#
data[mask]

# assign all vals < 0 to be 0
data[data<0]=0

# apply 1D 'names' array onto 7x4 'data' ndarray
data[names!="Joe"]=7
# data[-(names=="Joe")]=7
