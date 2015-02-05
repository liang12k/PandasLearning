import pandas
import numpy
import pylab

"""
 boolean indexing (numpy)
 -used as a "filter" on DataFrame by col(s) | think qztable[__filter__]
"""

# set default pandas option - display max 10 rows; first/last 5
pandas.set_option("display.max_rows",10)

# %pylab inline

auto = pandas.read_csv("auto.csv")
# print auto
# print auto.head()
# print auto.tail()
"""
         make  price  mpg  repairs  weight  length  foreign
0         AMC   4099   22        3    2930     186        0
1         AMC   4749   17        3    3350     173        0
2         AMC   3799   22        3    2640     168        0
3        Audi   9690   17        5    2830     189        1
4        Audi   6295   23        3    2070     174        1
..        ...    ...  ...      ...     ...     ...      ...
21  Chevrolet   3955   19        3    3430     197        0
22     Datsun   6229   23        4    2370     170        1
23     Datsun   4589   35        5    2020     165        1
24     Datsun   5079   24        4    2280     170        1
25     Datsun   8129   21        4    2750     184        1

[26 rows x 7 columns]
"""

# search in column "foreign" for value == 1
# print auto.foreign == 1 
# returns boolean index
# for "foreign" col, bool val per cell displayed
"""
0    False
1    False
2    False
...
23    True
24    True
25    True
Name: foreign, Length: 26, dtype: bool
"""

# set variable "mask" to the search filter
mask = auto.foreign==1
# print auto[mask] # apply mask to DataFrame for filtered data set
"""
      make  price  mpg  repairs  weight  length  foreign
3     Audi   9690   17        5    2830     189        1
4     Audi   6295   23        3    2070     174        1
5      BMW   9735   25        4    2650     177        1
22  Datsun   6229   23        4    2370     170        1
23  Datsun   4589   35        5    2020     165        1
24  Datsun   5079   24        4    2280     170        1
25  Datsun   8129   21        4    2750     184        1
"""

foreign = auto[mask]
# print foreign

# apply inverse filter
# numpy reverse the index
domestic = auto[numpy.invert(mask)] # == auto[auto.foreign!=1]
print domestic
"""
         make  price  mpg  repairs  weight  length  foreign
0         AMC   4099   22        3    2930     186        0
1         AMC   4749   17        3    3350     173        0
2         AMC   3799   22        3    2640     168        0
6       Buick   4816   20        3    3250     196        0
7       Buick   7827   15        4    4080     222        0
..        ...    ...  ...      ...     ...     ...      ...
17  Chevrolet   5705   16        4    3690     212        0
18  Chevrolet   4504   22        3    3180     193        0
19  Chevrolet   5104   22        2    3220     200        0
20  Chevrolet   3667   24        2    2750     179        0
21  Chevrolet   3955   19        3    3430     197        0
"""

# and condition filter
# NOTE: the parenthesis, keyword "and" not recognized
mpgpriceFilter = ((auto.mpg>20) & (auto.price<5000))
print auto[mpgpriceFilter]
"""
         make  price  mpg  repairs  weight  length  foreign
0         AMC   4099   22        3    2930     186        0
2         AMC   3799   22        3    2640     168        0
9       Buick   4453   26        3    2230     170        0
16  Chevrolet   3299   29        3    2110     163        0
18  Chevrolet   4504   22        3    3180     193        0
20  Chevrolet   3667   24        2    2750     179        0
23     Datsun   4589   35        5    2020     165        1
"""
