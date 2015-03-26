import pandas
import numpy
import pylab

"""
 DataFrame - data selections examples, specific/all of rows/cols ranges
"""

# %pylab inline

# # time-series
# generating a range of dates
days = pandas.date_range("2014-01-01", "2014-02-28", freq="D")

dim = (59,5) # array dimensons

dataframe = pandas.DataFrame(
                numpy.random.random_integers(-20,40,dim),
                index=days,
                columns=["Madrid","Boston","Tokyo","Shanghai","Kolkata"]
            )
# print dataframe
# print dataframe.head() 
# print dataframe.tail()

# row, col range
# print dataframe.ix[3:6, "Madrid":"Tokyo"]
"""
            Madrid  Boston  Tokyo
2014-01-04      40      13     -3
2014-01-05       5      32     25
2014-01-06      16      30     18
"""

# specific rows, range of cols
#print dataframe.ix[[7,31,40],"Madrid":"Shanghai"]
"""
            Madrid  Boston  Tokyo  Shanghai
2014-01-08      37      -4     -6        32
2014-02-01       2      34    -16        19
2014-02-10       2      37     19        -6
"""

# specific rows, specific cols
# print dataframe.ix[[3,20,49],["Boston","Shanghai"]]
"""
            Boston  Shanghai
2014-01-04      19        28
2014-01-21     -19        24
2014-02-19      -9        -6
"""

# specific rows, all cols
# print dataframe.ix[[3,20,49],:]
"""
            Madrid  Boston  Tokyo  Shanghai  Kolkata
2014-01-04      33       4     18        20       22
2014-01-21       7      17     -6        25       32
2014-02-19      26      21     -3         9      -16
"""

# all rows, range of cols
print dataframe.ix[:,"Boston":"Shanghai"]

# range of rows, specific cols
print dataframe.ix[3:11,["Boston","Shanghai"]]
"""
            Boston  Shanghai
2014-01-04      20        -6
2014-01-05       1        -3
2014-01-06     -20       -18
2014-01-07      -9        -2
2014-01-08      28       -12
2014-01-09     -13        36
2014-01-10     -19         2
2014-01-11      16        21
"""

