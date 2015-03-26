"""
exporting data to delimited format
.to_csv, .from_csv
"""

import sys
import numpy as np
import pandas as pd

data=pd.read_csv("ex5.csv"); data
'''
  something  a   b   c   d message
0       one  1   2   3   4     NaN
1       two  5   6 NaN   8   world
2     three  9  10  11  12     foo
'''
# data.to_csv("ex5_out.csv")
# data.to_csv("ex5_out_delimited.csv",sep="|")

data.to_csv(sys.stdout, na_rep="NULL")
# replace NaN w 'NULL' value
'''
,something,a,b,c,d,message
0,one,1,2,3.0,4,NULL
1,two,5,6,NULL,8,world
2,three,9,10,11.0,12,foo
'''
data.to_csv(sys.stdout, index=False, header=False)
# disable writing index, header names
'''
one,1,2,3.0,4,
two,5,6,,8,world
three,9,10,11.0,12,foo
'''
data.to_csv(
    sys.stdout,
    index=False,
    columns=list("abc")
)
# get select cols
'''
a,b,c
1,2,3.0
5,6,
9,10,11.0
'''

# # Series .to_csv method
dates=pd.date_range("1/1/2000",periods=7)
dates
'''
<class 'pandas.tseries.index.DatetimeIndex'>
[2000-01-01, ..., 2000-01-07]
Length: 7, Freq: D, Timezone: None
'''
ts=pd.Series(np.arange(7), index=dates)
ts
'''
2000-01-01    0
2000-01-02    1
2000-01-03    2
2000-01-04    3
2000-01-05    4
2000-01-06    5
2000-01-07    6
Freq: D, dtype: int64
'''
# ts.to_csv("tseries.csv")
pd.Series.from_csv("tseries.csv", parse_dates=True)
'''
2000-01-01    0
2000-01-02    1
2000-01-03    2
2000-01-04    3
2000-01-05    4
2000-01-06    5
2000-01-07    6
dtype: int64
'''
