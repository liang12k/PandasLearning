"""
'level': option in summary statistics methods
"""

import pandas as pd
from reorderingsortinglevels import frame

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
frame.sum(level="key1")
'''
state  Ohio     Colorado
color Green Red    Green
key1
a         3   5        7
b        15  17       19
'''
frame.sum(level="key2")
# **note: axis default to 0
'''
state  Ohio     Colorado
color Green Red    Green
key1
a         3   5        7
b        15  17       19
'''
frame.sum(level="state",axis=1)
# **note: need to set axis=1, default to 0
'''
state      Colorado  Ohio
key1 key2
a    1            2     1
     2            5     7
b    1            8    13
     2           11    19
'''
frame.sum(level="color",axis=1)
'''
color      Green  Red
key1 key2
a    1         2    1
     2         8    4
b    1        14    7
     2        20   10
'''
frame.cumsum()
'''
state      Ohio     Colorado
color     Green Red    Green
key1 key2
a    1        0   1        2
     2        3   5        7
b    1        9  12       15
     2       18  22       26
'''
frame.cumsum(1)
'''
state      Ohio     Colorado
color     Green Red    Green
key1 key2
a    1        0   1        3
     2        3   7       12
b    1        6  13       21
     2        9  19       30
'''

