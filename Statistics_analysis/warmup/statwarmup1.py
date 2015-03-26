import pandas
import numpy
import pylab

"""
 basic statistic analysis on auto.csv
 -getting description of table; mean, std dev, min, max...
 -getting median, std dev for single col name
 -plotting histogram
"""

# setting default max 20 rows to display 
pandas.set_option("display.max_rows",20)

auto = pandas.read_csv("auto.csv")
# print auto.head()
"""
   make  price  mpg  repairs  weight  length  foreign
0   AMC   4099   22        3    2930     186        0
1   AMC   4749   17        3    3350     173        0
2   AMC   3799   22        3    2640     168        0
3  Audi   9690   17        5    2830     189        1
4  Audi   6295   23        3    2070     174        1
"""

# print auto.describe()
"""
              price        mpg    repairs       weight      length    foreign
count     26.000000  26.000000  26.000000    26.000000   26.000000  26.000000
mean    6651.730769  20.923077   3.269231  3099.230769  190.076923   0.269231
std     3371.119809   4.757504   0.777570   695.079409   18.170136   0.452344
min     3299.000000  14.000000   2.000000  2020.000000  163.000000   0.000000
25%     4465.750000  17.250000   3.000000  2642.500000  173.250000   0.000000
50%     5146.500000  21.000000   3.000000  3200.000000  191.000000   0.000000
75%     8053.500000  23.000000   4.000000  3610.000000  203.000000   0.750000
max    15906.000000  35.000000   5.000000  4330.000000  222.000000   1.000000
"""

# print auto.mpg.describe() # statistic info only on mpg col
# Note: if col name has spaces, do: DataFrame["_col name_"].describe()
"""
count    26.000000
mean     20.923077
std       4.757504
min      14.000000
25%      17.250000
50%      21.000000
75%      23.000000
max      35.000000
Name: mpg, dtype: float64
"""

# print auto.mpg.median(), auto.mpg.std()
# median = 21.0, std deviation = 4.75750419378

# plotting a histogram
# # Note: no title arg, need pylab.suptitle for title insertion into histogram
# auto.mpg.hist(); pylab.suptitle("Automobiles - mpg histogram"); pylab.show()
# auto.price.hist(); pylab.suptitle("Automobiles - price histogram"); pylab.show()

# box plot
auto.boxplot(column="price"); pylab.show()
# low bar = min
# high bar = max
# red bar = median
# box = 25% to 75% quartile

