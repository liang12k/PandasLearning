"""
.set_index: new DataFrame using 1+ col as index

.reset_index: hierarchical index levels moved
              into cols
"""

import pandas as pd
from pandas import DataFrame, Series

frame=DataFrame(
    {
        "a":range(7),
        "b":range(7,0,-1), # reverse order
        "c":["one"]*3+["two"]*4,
        "d":[0,1,2,0,1,2,3]
    }
)
frame
'''
   a  b    c  d
0  0  7  one  0
1  1  6  one  1
2  2  5  one  2
3  3  4  two  0
4  4  3  two  1
5  5  2  two  2
6  6  1  two  3
'''
frame2=frame.set_index(["c","d"]); frame2
# unique pairs of 'c','d' as indexes
'''
       a  b
c   d
one 0  0  7
    1  1  6
    2  2  5
two 0  3  4
    1  4  3
    2  5  2
    3  6  1
'''
frame.set_index(["c","d"],drop=False)
# keep the col(s) set as index(es) in DataFrame
'''
       a  b    c  d
c   d
one 0  0  7  one  0
    1  1  6  one  1
    2  2  5  one  2
two 0  3  4  two  0
    1  4  3  two  1
    2  5  2  two  2
    3  6  1  two  3
'''
frame2.reset_index()
'''
     c  d  a  b
0  one  0  0  7
1  one  1  1  6
2  one  2  2  5
3  two  0  3  4
4  two  1  4  3
5  two  2  5  2
6  two  3  6  1
'''
frame.reset_index()
# note: default to numbers as indexes in rows
'''
   index  a  b    c  d
0      0  0  7  one  0
1      1  1  6  one  1
2      2  2  5  one  2
3      3  3  4  two  0
4      4  4  3  two  1
5      5  5  2  two  2
6      6  6  1  two  3
'''
frame.index
# Int64Index([0, 1, 2, 3, 4, 5, 6], dtype='int64')
