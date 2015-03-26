import pandas, numpy

__doc__ = """
Series is a subclass of ndarray; 
valid arugment to most numpy functions
ex:
 Series.median
 Series.cumsum # returns cumulative sum of elems along given axis
               # http://docs.scipy.org/doc/numpy/reference/generated/numpy.cumsum.html
"""

d1 = {"Mon":33, "Tue":19, "Wed":15, "Thu":89, "Fri":11, "Sat":-5, "Sun":9}
s7 = pandas.Series(d1)
s7[1] = 199

print s7.median() # 15.0

print s7.max() # 199

print s7.cumsum()
'''
Fri     11
Mon    210
Sat    205
Sun    214
Thu    303
Tue    322
Wed    337
dtype: int64
'''
