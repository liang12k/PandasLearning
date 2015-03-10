"""

"""

import numpy as np
import pandas as pd
from string import ascii_lowercase

obj=pd.Series(
    np.arange(4.),
    index=[_ for _ in ascii_lowercase[:4]]
)
obj
# a    0
# b    1
# c    2
# d    3
# dtype: float64
obj["b"]
# 1.0
obj[1]
# 1.0
# obj[2:4]
# c    2
# d    3
# dtype: float64
obj[["b","a","d"]] # specific row order
# b    1
# a    0
# d    3
# dtype: float64
obj[[1,2]] # row specific
# b    1
# c    2
# dtype: float64
obj[obj < 2] # apply filtering on rows
# a    0
# b    1
# dtype: float64
obj["b":"c"] # slicing
# b    1
# c    2
# dtype: float64
obj["b":"c"]=5 # setting value
# a    0
# b    5
# c    5
# d    3
# dtype: float64

# # DataFrame - indexing for retrieving 1+ cols
# #             with either single value or sequence
data=pd.DataFrame(
    np.arange(16).reshape((4,4)),
    index=["Ohio","Colorado","Utah","New York"],
    columns=["one","two","three","four"]
)
data
#           one  two  three  four
# Ohio        0    1      2     3
# Colorado    4    5      6     7
# Utah        8    9     10    11
# New York   12   13     14    15
data["two"]
# Ohio         1
# Colorado     5
# Utah         9
# New York    13
# Name: two, dtype: int64
data[["three","one"]]
#           three  one
# Ohio          2    0
# Colorado      6    4
# Utah         10    8
# New York     14   12
#
# # special cases for indexing
