import pandas, numpy

__doc__ = """learning about Series slicing; geting values via offset"""

d1 = {"Mon":33, "Tue":19, "Wed":15, "Thu":89, "Fri":11, "Sat":-5, "Sun":9}

s6 = pandas.Series(d1)
print s6
'''
Fri    11
Mon    33
Sat    -5
Sun     9
Thu    89
Tue    19
Wed    15
'''

print s6["Thu":"Wed"] # [inclusive start:inclusive end]
'''
Thu    89
Tue    19
Wed    15
dtype: int64
'''

print s6[1:3] # [inclusive, exclusive]
'''
Mon    33
Sat    -5
dtype: int64
'''

print s6[1] # 33 # this only gets the value at this index

# setting value using offset
s6[1] = 199
print s6
'''
Fri     11
Mon    199
Sat     -5
Sun      9
Thu     89
Tue     19
Wed     15
dtype: int64
'''

