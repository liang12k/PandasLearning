import pandas
import datetime

"""
pandas.DataFrame:
 -2D array: row/col each has labels, indices
 -any datatype in array; homogenous values
"""

startdate = datetime.datetime(2013,12,1)
enddate = datetime.datetime(2013,12,8)
stepdays = datetime.timedelta(days=1)
dateslist = []

while startdate < enddate:
    dateslist.append(startdate.strftime("%m-%d"))
    startdate += stepdays
# print dateslist

tableAsDict = {
    "Date":dateslist,
    "Mumbai":[20,18,23,19,25,27,23],
    "Paris":[-2,0,2,5,7,-5,-3],
    "Tokyo":[15,19,15,11,9,8,13],
}
dframe = pandas.DataFrame(tableAsDict)
print dframe
"""
    Date  Mumbai  Paris  Tokyo
0  12-01      20     -2     15
1  12-02      18      0     19
2  12-03      23      2     15
3  12-04      19      5     11
4  12-05      25      7      9
5  12-06      27     -5      8
6  12-07      23     -3     13
"""

print dframe.Mumbai # == dframe["Mumbai"]
"""
0    20
1    18
2    23
3    19
4    25
5    27
6    23
Name: Mumbai, dtype: int64
"""
print type(dframe["Mumbai"]) # <class 'pandas.core.series.Series'>

dframe = dframe.set_index("Date") 
# "Date" col is the index, no numerical indexes on the left
print dframe
"""
Date
12-01      20     -2     15
12-02      18      0     19
12-03      23      2     15
12-04      19      5     11
12-05      25      7      9
12-06      27     -5      8
12-07      23     -3     13
"""

