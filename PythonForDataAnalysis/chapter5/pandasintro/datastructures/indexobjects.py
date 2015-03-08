"""
pandas's Index objects hold axis lates and
other metadata (ie: axis names)
-array or other sequence of labels used when
 constructing Series, DataFrame internally
 converted to an Index
-array-like and functions as fixed-size set
-** index objects are immutable to be safely 
    shared among data structures
"""

import pandas as pd
import numpy as np

obj=pd.Series(range(3),index=["a","b","c"])
index=obj.index
index # Index([u'a', u'b', u'c'], dtype='object')
index[1:] # Index([u'b', u'c'], dtype='object')
# index objs are immutable, this'll throw error
# index[1]="d"

index=pd.Index(np.arange(3))
obj2=pd.Series([1.5,-2.5,0],index=index)
obj2
# 0    1.5
# 1   -2.5
# 2    0.0
# dtype: float64
#
# '==' checks dict of values --> bool array returned
obj2.index is index, obj2.index==index
# True , array([ True,  True,  True], dtype=bool)

# Index object as fixed-size set
from dataframe_examples import frame3
frame3
# state  Nevada  Ohio
# year
# 2000      NaN   1.5
# 2001      2.4   1.7
# 2002      2.9   3.6
"Ohio" in frame3.columns, 2003 in frame3.index
# True , False

# # 
# # Table5-2
# # main Index objects in pandas
# # 
{'DatetimeIndex': "Stores nanosecond timestamps (represented using NumPy's datetime64 dtype).",
 'Index': 'The most general Index object, representing axis labels in a NumPy array of Python objects.',
 'Int64Index': 'Specialized Index for integer values.',
 'MultiIndex': "'Hierarchical' index object representing multiple levels of indexing on a single axis. Can be thought of as similar to an array of tuples.",
 'PeriodIndex': 'Specialized Index for Period data (timespans).'}

# # 
# # Table5-3
# # Index methods and properties
# # -note: Index objects behave array-like, set like
# # 
{'append': 'Concatenate with additional Index objects, producing a new Index diff Compute set difference as an Index',
 'drop': 'Compute new index by deleting passed values',
 'insert': 'Compute new Index by inserting element at index i',
 'intersection': 'Compute set intersection',
 'is_monotonic': 'Returns True if each element is greater than or equal to the previous element is_unique Returns True if the Index has no duplicate values',
 'isin': 'Compute boolean array indicating whether each value is contained in the passed collection delete Compute new Index with element at index i deleted',
 'union': 'Compute set union',
 'unique': 'Compute the array of unique values in the Index'}
