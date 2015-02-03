import pandas
# import numpy
import pylab

"""
 using mortality.csv
 -learning Transpose (DataFrame.T)
"""

# row idx autom generated
mort = pandas.read_csv("mortality.csv")

# print mort.columns.values.tolist() # == list(mort.columns.values)
"""
col names: Country Name', '1960',...,'2013'
"""
# # [5 rows x 55 columns]
# print mort.head() 
# print mort.tail()

mort = mort.set_index("Country Name")

# # transpose : rows <--> cols
t = mort.T
# print t.head() # [5 rows x 224 columns]

# select cols
cmp = t[["Bangladesh","India","Rwanda","Uganda"]]
# print cmp
# print cmp.head()
"""
Country Name  Bangladesh  India  Rwanda  Uganda
1960               262.4  246.3   214.5   224.4
1961               255.3  242.2   209.8   219.5
1962               248.4  238.1   206.2   214.1
1963               241.9  234.6   204.2   209.1
1964               235.9  231.1   203.0   204.0
"""
# print cmp.tail()
"""
Country Name  Bangladesh  India  Rwanda  Uganda
2009                50.9   63.8    69.4    83.0
2010                47.2   61.2    63.8    78.3
2011                43.8   58.6    58.9    74.0
2012                40.9   56.3    55.0    68.9
2013                 NaN    NaN     NaN     NaN
"""

cmp.plot(title="Mortality Rate: %s" % str(cmp.columns.values.tolist()))
pylab.show()
