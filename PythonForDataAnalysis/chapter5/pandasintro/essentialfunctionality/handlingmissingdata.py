"""
NaN: missing data default value (== None value)
     -a sentinel for easy detection
     -aka: flag value, signal value
     >sentinel: http://en.wikipedia.org/wiki/Sentinel_value
     > http://www.webopedia.com/TERM/S/sentinel_value.html
     : special value guarantees termination
     : not a 'legitimate' value in loop
"""

import numpy as np
import pandas as pd

stringdata=pd.Series(
    ["aardvark","artichoke",np.nan,"avocado"]
)
stringdata
# 0     aardvark
# 1    artichoke
# 2          NaN
# 3      avocado
# dtype: object
stringdata.isnull()
# 0    False
# 1    False
# 2     True
# 3    False
# dtype: bool
stringdata[0]=None # == np.nan (NaN)
stringdata
# 0         None
# 1    artichoke
# 2          NaN
# 3      avocado
# dtype: object
stringdata.isnull()
# 0     True
# 1    False
# 2     True
# 3    False
# dtype: bool
stringdata.dropna()
# 1    artichoke
# 3      avocado
# dtype: object
stringdata.fillna("shoop")
# 0        shoop
# 1    artichoke
# 2        shoop
# 3      avocado
# dtype: object


# # Table5-12: NaN handling methods
{'dropna': 'Filter axis labels based on whether values for each label have missing data, with varying thresholds for how much missing data to tolerate',
 'fillna': "Fill in missing data with some value or using an interpolation method such as 'ffill' or 'bfill'",
 'isnull': 'Return like-type object containing boolean values indicating which values are missing / NA',
 'notnull': 'Negation of isnull'}
