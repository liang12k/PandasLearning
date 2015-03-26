import pandas

__doc__ = """creating a Series through a python dict; passing data=dict"""

d1 = {"Mon":33, "Tue":19, "Wed":15, "Thu":89, "Fri":11, "Sat":-5, "Sun":9}
# able to take the dict and dtermine the keys, vals
s4 = pandas.Series(d1) # ==  pandas.Series(d1.values(), index=d1.keys())
print s4
'''
Wed    15
Sun     9
Fri    11
Tue    19
Mon    33
Thu    89
Sat    -5
dtype: int64
'''
