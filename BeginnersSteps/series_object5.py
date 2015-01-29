import pandas
import numpy

__doc__ = """doing some vector operations; Series*2, numpy.log(Series)"""

d1 = {"Mon":33, "Tue":19, "Wed":15, "Thu":89, "Fri":11, "Sat":-5, "Sun":9}
# able to take the dict and determine the keys, vals
s5 = pandas.Series(d1)

print s5
'''
Fri    11
Mon    33
Sat    -5
Sun     9
Thu    89
Tue    19
Wed    15
dtype: int64
'''

# # vectorized operations
print s5*2 # multiples the values; scalar
'''
Fri     22
Mon     66
Sat    -10
Sun     18
Thu    178
Tue     38
Wed     30
'''

print numpy.log(s5)
'''
Fri    2.397895
Mon    3.496508
Sat         NaN
Sun    2.197225
Thu    4.488636
Tue    2.944439
Wed    2.708050
dtype: float64
'''
