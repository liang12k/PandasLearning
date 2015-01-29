import pandas
import numpy

# Series: obj has array + dict like properties
# -access via indexes, keys
# -"amphibian" object
# -mapping of index-to-values

s1 = pandas.Series([33, 19, 89, 11, -5, 9])

print s1
'''
0    33
1    19
2    89
3    11
4    -5
5     9
dtype: int64
'''

print type(s1) # <class 'pandas.core.series.Series'>

print s1.values # [33 19 89 11 -5  9]
print type(s1.values) # <type 'numpy.ndarray'>

print s1.index # Int64Index([0, 1, 2, 3, 4, 5], dtype='int64')



