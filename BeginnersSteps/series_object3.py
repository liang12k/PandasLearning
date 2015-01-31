import pandas
import numpy

__doc__ = """learning about Series being homogenous; values are numerical"""

# values are homogenous; note the float num idx 1
vals_nums = [33, 19.3, 15, 89, 11, -5, 9]
index_strs = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

s3 = pandas.Series(vals_nums, index=index_strs)
print s3
'''
# note the values are now float64 types
Mon    33.0
Tue    19.3
Wed    15.0
Thu    89.0
Fri    11.0
Sat    -5.0
Sun     9.0
dtype: float64
'''
