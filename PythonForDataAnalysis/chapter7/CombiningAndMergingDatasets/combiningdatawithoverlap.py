"""
numpy .where
-returns elems from x or y, depending on a condition
-http://docs.scipy.org/doc/numpy/reference/generated/numpy.where.html
"""

import numpy as np
import pandas as pd

a=pd.Series(
    [np.nan,2.5,np.nan,3.5,4.5,np.nan],
    index=list("fedcba")
)
b=pd.Series(
    np.arange(len(a), dtype=np.float64),
    index=list("fedcba")
)
b[-1]=np.nan
# print a
'''
f    NaN
e    2.5
d    NaN
c    3.5
b    4.5
a    NaN
dtype: float64
'''
# print b
'''
f     0
e     1
d     2
c     3
b     4
a   NaN
dtype: float64
'''
whereresult=np.where(pd.isnull(a),b,a)
# print whereresult
'''
[ 0.   2.5  2.   3.5  4.5  nan]
'''
# print pd.DataFrame(whereresult)
'''
     0
0  0.0
1  2.5
2  2.0
3  3.5
4  4.5
5  NaN
'''
