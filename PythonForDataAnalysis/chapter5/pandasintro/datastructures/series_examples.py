"""
series: 1D array-like obj containing array of data
        and an index (data labels)
"""

import numpy as np
import pandas as pd

# simplest Series formed
obj=pd.Series([4,7,-5,3])
obj
# 0    4
# 1    7
# 2   -5
# 3    3
# dtype: int64
obj.values
# array([ 4,  7, -5,  3])
obj.index
# # default index col of indices
# Int64Index([0, 1, 2, 3], dtype='int64')
#
# # altering Series in place
obj.index=["Bob","Steve","Jeff","Ryan"]
obj
# Bob      6
# Steve    7
# Jeff    -5
# Ryan     3
# dtype: int64
#
# getting specific output indicies order
obj[["Jeff","Bob","Ryan","Steve"]]
# Jeff    -5
# Bob      6
# Ryan     3
# Steve    7
# dtype: int64

obj2=pd.Series(obj.values,index=["d","b","a","c"])
obj2
# d    4
# b    7
# a   -5
# c    3
# dtype: int64
obj2["a"]
# -5
obj2["d"]=6
obj2[["c","a","d"]]
# c    3
# a   -5
# d    6
# dtype: int64
obj2
# d    6
# b    7
# a   -5
# c    3
# dtype: int64
obj2[obj2>0] # values > 0
# d    6
# b    7
# c    3
# dtype: int64
obj2*2
# d    12
# b    14
# a   -10
# c     6
# dtype: int64
np.exp(obj2)
# d     403.428793
# b    1096.633158
# a       0.006738
# c      20.085537
# dtype: float64
"b" in obj2, "e" in obj2
# (True, False)

# # creating series from python dict
# # -keys are the indices & sorted
sdata={
    "Ohio":35000,
    "Texas":71000,
    "Oregon":16000,
    "Utah":5000
}
obj3=pd.Series(sdata)
obj3
# Ohio      35000
# Oregon    16000
# Texas     71000
# Utah       5000
# dtype: int64

# # note: 'California' isn't in sdata
# #       it will be a Not-a-Number (NaN)
states=["California","Ohio","Oregon","Texas"]
obj4=pd.Series(sdata,index=states)
obj4
# California      NaN
# Ohio          35000
# Oregon        16000
# Texas         71000
# dtype: float64
pd.isnull(obj4)
# # same as: obj4.isnull()
# California     True
# Ohio          False
# Oregon        False
# Texas         False
# dtype: bool
pd.notnull(obj4)
# California    False
# Ohio           True
# Oregon         True
# Texas          True
# dtype: bool
#
# # arithm operation '+'
# # combine same index values, others are NaN
obj3+obj4
# California       NaN
# Ohio           70000
# Oregon         32000
# Texas         142000
# Utah             NaN
# dtype: float64
#
# # assigning series' title and index name
obj4.name="population"
obj4.index.name="state"
obj4
# state
# California      NaN
# Ohio          35000
# Oregon        16000
# Texas         71000
# Name: population, dtype: float64

