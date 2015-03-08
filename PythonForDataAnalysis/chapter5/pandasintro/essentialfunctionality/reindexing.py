"""
.reindex - operating on pandas objects
           create new object with data conformed
           to a new index
         - 'method' arg to handle interpolation
"""

import pandas as pd
import numpy as np

obj=pd.Series(
    [4.5,7.2,-5.3,3.6],
    index=["d","b","a","c"]
)
obj
# d    4.5
# b    7.2
# a   -5.3
# c    3.6
# dtype: float64
#
# # pd.Series.reindex rearranges data according
# # to new index
# # missing values introduced for DNE index values
#
# 'e' index DNE 
obj2=obj.reindex(["a","b","c","d","e"])
obj2
# a   -5.3
# b    7.2
# c    3.6
# d    4.5
# e    NaN
# dtype: float64
#
# fill in NaN values of reindex
obj.reindex(
    obj2.index,
    fill_value=0
)
# a   -5.3
# b    7.2
# c    3.6
# d    4.5
# e    0.0
# dtype: float64

# # ordered data (ie: time series)
# # do some interpolation (alter data by
# # inserting new data), filling of values
# # when reindexing
# # 'method' arg option allows filling holes in
# # reindexed data - methods are:
# # -ffill, pad : fill, carry values forward
# # -bfill, backfill: fill, carry values backward
#
obj3=pd.Series(
    ["blue","purple","yellow"],
    index=[0,2,4]
)
obj3.reindex(range(6))
# 0      blue
# 1       NaN
# 2    purple
# 3       NaN
# 4    yellow
# 5       NaN
# dtype: object
#
# # taking the latest value before blank NaN index value
# # plug into NaN
obj3ffill=obj3.reindex(range(6),method="ffill")
# 0      blue
# 1      blue
# 2    purple
# 3    purple
# 4    yellow
# 5    yellow
# dtype: object
#
# # taking latest value after blank NaN index value
# # plug into NaN
obj3bfill=obj3.reindex(range(6),method="bfill")
# 0      blue
# 1    purple
# 2    purple
# 3    yellow
# 4    yellow
# 5       NaN
# dtype: object

# #
# # Table5-4
# # .reindex 'method' (interpolation) arg options
# ffill, pad - fill, carry values forward
#              taking latest value before blank NaN
#              value, plug that into NaN
# bfill, backfill - fill, carry values backward
#                   taking latest value after blank NaN
#                   value, plug that into NaN

