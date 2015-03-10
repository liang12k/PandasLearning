"""
.drop - drop indices based on axis arg
        **note: new obj is returned
                set 'inplace' arg to True if needed
"""

import numpy as np
import pandas as pd
from string import ascii_lowercase

obj=pd.Series(
    np.arange(5.),
    index=[_ for _ in ascii_lowercase[:5]]
)
# a    0
# b    1
# c    2
# d    3
# e    4
# dtype: float64
#
# # .drop index
new_obj=obj.drop("c"); new_obj
# a    0
# b    1
# d    3
# e    4
# dtype: float64
#
obj.drop(["d","c"])
# a    0
# b    1
# e    4
# dtype: float64

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
data.drop(["Colorado","Ohio"])
#           one  two  three  four
# Utah        8    9     10    11
# New York   12   13     14    15

# # row drop
data.drop(["New York","Ohio"],axis=0)
#           one  two  three  four
# Colorado    4    5      6     7
# Utah        8    9     10    11

# # col drop
data.drop(["three","four"],axis=1)
#          one  two
# Ohio        0    1
# Colorado    4    5
# Utah        8    9
# New York   12   13

