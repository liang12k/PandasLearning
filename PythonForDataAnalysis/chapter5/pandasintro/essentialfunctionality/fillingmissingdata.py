"""
.fillna : filling in missing data w a value
          -returns new obj, or can modify in place
"""

import numpy as np
from numpy import nan as NA
import pandas as pd
from filterout_missingdata import df

df
'''
          0         1         2
0 -1.090359       NaN       NaN
1  0.032439       NaN       NaN
2  0.988118       NaN       NaN
3 -0.961177       NaN  1.360733
4  0.250723       NaN  0.236338
5  1.090097  1.629183  1.635893
6 -0.691680 -0.193164  0.510624
'''
df.fillna(0)
'''
          0         1         2
0 -1.090359  0.000000  0.000000
1  0.032439  0.000000  0.000000
2  0.988118  0.000000  0.000000
3 -0.961177  0.000000  1.360733
4  0.250723  0.000000  0.236338
5  1.090097  1.629183  1.635893
6 -0.691680 -0.193164  0.510624
'''
df.fillna({1:0.5, 3:-1})
# fill na values for cols (key name = col index)
'''
0 -1.090359  0.500000       NaN
1  0.032439  0.500000       NaN
2  0.988118  0.500000       NaN
3 -0.961177  0.500000  1.360733
4  0.250723  0.500000  0.236338
5  1.090097  1.629183  1.635893
6 -0.691680 -0.193164  0.510624
'''
_df=df.fillna(0,inplace=True)
_df
'''
          0         1         2
0 -1.090359  0.500000       NaN
1  0.032439  0.500000       NaN
2  0.988118  0.500000       NaN
3 -0.961177  0.500000  1.360733
4  0.250723  0.500000  0.236338
5  1.090097  1.629183  1.635893
6 -0.691680 -0.193164  0.510624
'''
df
'''
0 -1.090359  0.000000  0.000000
1  0.032439  0.000000  0.000000
2  0.988118  0.000000  0.000000
3 -0.961177  0.000000  1.360733
4  0.250723  0.000000  0.236338
5  1.090097  1.629183  1.635893
6 -0.691680 -0.193164  0.510624
'''
df=pd.DataFrame(np.random.randn(6,3))
df
'''
          0         1         2
0  0.258942  1.715273 -0.142848
1 -0.093323  1.857927  0.032534
2  1.494509  0.397160  0.021675
3 -2.062789 -1.026491  0.553108
4 -0.910356 -0.568210 -0.698382
5  1.342794  2.648429 -0.210584
'''
# # interpolation methods (slicing)
# #
df.ix[2:,1]=NA; df
# col 1, rows 2:end, assign NA
'''
          0         1         2
0  0.258942  1.715273 -0.142848
1 -0.093323  1.857927  0.032534
2  1.494509       NaN  0.021675
3 -2.062789       NaN  0.553108
4 -0.910356       NaN -0.698382
5  1.342794       NaN -0.210584
'''
df.ix[4:,2]=NA; df
# col 2, rows 4:end, assign NA
'''
          0         1         2
0  0.258942  1.715273 -0.142848
1 -0.093323  1.857927  0.032534
2  1.494509       NaN  0.021675
3 -2.062789       NaN  0.553108
4 -0.910356       NaN       NaN
5  1.342794       NaN       NaN
'''
df.fillna(method="ffill")
# ffill: take previous value and
#        replace next  NaN value
# **note: bfill is pointless as NaN values are
#         consistent in order
'''
          0         1         2
0  0.258942  1.715273 -0.142848
1 -0.093323  1.857927  0.032534
2  1.494509  1.857927  0.021675
3 -2.062789  1.857927  0.553108
4 -0.910356  1.857927  0.553108
5  1.342794  1.857927  0.553108
'''
df.fillna(method="ffill",limit=1)
# fillna at most 1 NaN value
'''
          0         1         2
0  0.258942  1.715273 -0.142848
1 -0.093323  1.857927  0.032534
2  1.494509  1.857927  0.021675
3 -2.062789       NaN  0.553108
4 -0.910356       NaN  0.553108
5  1.342794       NaN       NaN
'''
df.fillna(method="ffill",limit=2)
# fillna at most 2 NaN values
'''
          0         1         2
0  0.258942  1.715273 -0.142848
1 -0.093323  1.857927  0.032534
2  1.494509  1.857927  0.021675
3 -2.062789  1.857927  0.553108
4 -0.910356       NaN  0.553108
5  1.342794       NaN  0.553108
'''

data=pd.Series([1.,NA,3.5,NA,7])
data
# 0    1.0
# 1    NaN
# 2    3.5
# 3    NaN
# 4    7.0
# dtype: float64
data.fillna(data.mean()) # fillna w mean value
# 0    1.000000
# 1    3.833333
# 2    3.500000
# 3    3.833333
# 4    7.000000
# dtype: float64

# # Table5-13: reference on .fillna, args
{'axis': 'Axis to fill on, default axis=0',
 'inplace': 'Modify the calling object without producing a copy',
 'limit': 'For forward and backward filling, maximum number of consecutive periods to fill',
 'method': "Interpolation, by default 'ffill' if function called with no other arguments",
 'value': 'Scalar value or dict-like object to use to fill missing values'}
