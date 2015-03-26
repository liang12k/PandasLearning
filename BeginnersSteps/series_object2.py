import pandas
import numpy

__doc__ = """creating a Series using num vals, str indexes"""

vals_nums = [33, 19, 15, 89, 11, -5, 9]
index_strs = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

s2 = pandas.Series(vals_nums, index=index_strs)
print s2
'''
Mon    33
Tue    19
Wed    15
Thu    89
Fri    11
Sat    -5
Sun     9
dtype: int64
'''

print s2.index
# Index([u'Mon', u'Tue', u'Wed', u'Thu', u'Fri', u'Sat', u'Sun'], dtype='object)

# # meaningful labels; series name and index 'col' name
s2.name = "Daily Temperatures"
s2.index.name = "Weekday"
print s2
'''
Weekday
Mon        33
Tue        19
Wed        15
Thu        89
Fri        11
Sat        -5
Sun         9
Name: Daily Temperatures, dtype: int64
'''
