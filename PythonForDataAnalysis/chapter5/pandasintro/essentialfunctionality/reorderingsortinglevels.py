"""
.swaplevel: takes two level numbers or names and
            returns a new object with levels
            interchanged (unaltered data)

.sortlevel: sorts data using only values in a
            single level
            lexicographically sorted, use on
            .swaplevel data
"""

import numpy as np
from numpy import nan as NA
import pandas as pd
from hierarchicalindexing import frame

frame
'''
state      Ohio     Colorado
color     Green Red    Green
key1 key2
a    1        0   1        2
     2        3   4        5
b    1        6   7        8
     2        9  10       11
'''
frame.index
'''
MultiIndex(levels=[[u'a', u'b'], [1, 2]],
           labels=[[0, 0, 1, 1], [0, 1, 0, 1]],
           names=[u'key1', u'key2'])
'''
frame.swaplevel("key1","key2")
# == frame.swaplevel(0,1)
'''
state      Ohio     Colorado
color     Green Red    Green
key2 key1
1    a        0   1        2
2    a        3   4        5
1    b        6   7        8
2    b        9  10       11
'''
frame.swaplevel("key1","key2")==frame.swaplevel(0,1)
'''
state      Ohio       Colorado
color     Green   Red    Green
key2 key1
1    a     True  True     True
2    a     True  True     True
1    b     True  True     True
2    b     True  True     True
'''
frame.sortlevel(1)
# 0 level = "a","b"
# 1 level = 1,2
'''
state      Ohio     Colorado
color     Green Red    Green
key1 key2
a    1        0   1        2
b    1        6   7        8
a    2        3   4        5
b    2        9  10       11
'''
frame.swaplevel(0,1).sortlevel(0)
# sort col 0 'key2'
'''
state      Ohio     Colorado
color     Green Red    Green
key2 key1
1    a        0   1        2
     b        6   7        8
2    a        3   4        5
     b        9  10       11
'''
frame.swaplevel(0,1).sortlevel(1)
# sort col 1 'key1'
# **note: all 'key2' values displayed
#         to stick with 'key1' values
'''
state      Ohio     Colorado
color     Green Red    Green
key2 key1
1    a        0   1        2
2    a        3   4        5
1    b        6   7        8
2    b        9  10       11
'''
