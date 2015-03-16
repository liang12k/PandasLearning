"""

"""

import numpy as np
import pandas as pd

obj=pd.Series(list("cadaabbcc"))
obj
# 0    c
# 1    a
# 2    d
# 3    a
# 4    a
# 5    b
# 6    b
# 7    c
# 8    c
# dtype: object
obj.value_counts()
# c    3
# a    3
# b    2
# d    1
# dtype: int64
obj.value_counts(sort=False)
# # supposed to be a,b,c,d
#   (diff from book, pd vers diff?)
# a    3
# c    3
# b    2
# d    1
# dtype: int64
unique=obj.unique()
unique
# array(['c', 'a', 'd', 'b'], dtype=object)

# # .isin: vectorized set membership
# #        -helps for filtering dataset down to
# #         subset of values in Series, DataFrame col
mask=obj.isin(["b","c"])
mask
# 0     True
# 1    False
# 2    False
# 3    False
# 4    False
# 5     True
# 6     True
# 7     True
# 8     True
# dtype: bool
obj[mask]
# return only values where 'True'
#
# 0    c
# 5    b
# 6    b
# 7    c
# 8    c
# dtype: object
m=obj=="a"; obj[m]
# 1    a
# 3    a
# 4    a
# dtype: object

# # getting histogram on multiple cols in DataFrame
data=pd.DataFrame(
    {
        "Qu1":[1,3,4,3,5],
        "Qu2":[2,3,1,2,3],
        "Qu3":[1,5,2,4,4]
    }
)
data
'''
   Qu1  Qu2  Qu3
0    1    2    1
1    3    3    5
2    4    1    2
3    3    2    4
4    5    3    4
'''
data.stack()
# # DataFrame.stack(): pivots level of DataFrame
# #                    as a single level
'''
0  Qu1    1
   Qu2    2
   Qu3    1
1  Qu1    3
   Qu2    3
   Qu3    5
2  Qu1    4
   Qu2    1
   Qu3    2
3  Qu1    3
   Qu2    2
   Qu3    4
4  Qu1    5
   Qu2    3
   Qu3    4
dtype: int64
'''
data.stack().value_counts()
# # from stack of values, get value_counts
#
# 3    4
# 4    3
# 2    3
# 1    3
# 5    2
# dtype: int64
data.apply(pd.value_counts)
# for each value, determine the counts
# of it in each column
'''
   Qu1  Qu2  Qu3
1    1    1    1
2  NaN    2    1
3    2    2  NaN
4    1  NaN    2
5    1  NaN    1
'''
data.apply(pd.value_counts).fillna(0)
# from above, replace NaN with 0
'''
   Qu1  Qu2  Qu3
1    1    1    1
2    0    2    1
3    2    2    0
4    1    0    2
5    1    0    1
'''

# # Table5-11: unique,value counts, binning methods
{'isin': 'Compute boolean array indicating whether each Series value is contained in the passed sequence of values.',
 'unique': 'Compute array of unique values in a Series, returned in the order observed.',
 'value_counts': 'Return a Series containing unique values as its index and frequencies as its values, ordered count in descending order.'}
