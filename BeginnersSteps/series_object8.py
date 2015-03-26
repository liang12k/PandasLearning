import pandas, numpy

__doc__ = """
Series - 'list','dict' operations
 looping
 list comprehension
 dict operations
"""

d1 = {"Mon":33, "Tue":19, "Wed":15, "Thu":89, "Fri":11, "Sat":-5, "Sun":9}
s8 = pandas.Series(d1)
s8[1] = 199

for i,v in enumerate(s8):
    print i,v
'''
0 11
1 199
2 -5
3 9
4 89
5 19
6 15
'''

new_list = [x**2 for x in s8]
print new_list # [121, 39601, 25, 81, 7921, 361, 225]

print "Sun" in s8 # True

# retrieve value via index|key
print s8["Tue"] # 19

s8["Tue"]=200
print s8
'''
Fri     11
Mon    199
Sat     -5
Sun      9
Thu     89
Tue    200
Wed     15
dtype: int64
'''

for k,v in s8.iteritems():
    print k,v
'''
Fri 11
Mon 199
Sat -5
Sun 9
Thu 89
Tue 200
Wed 15
'''

