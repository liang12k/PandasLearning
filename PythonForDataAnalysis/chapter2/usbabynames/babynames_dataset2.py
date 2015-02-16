import pandas as pd
import numpy as np
import pylab
from babynames_dataset1 import (top1000,boys,girls)

"""
US Baby Names 1880-2010
-----------------------
US Soc. Sec. Admin. (SSA) data on frequency of baby names
from 1880 through present (2010).

babynames_dataset2.py:
-measuring in/de-crease
-
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
reminder:
names = pd.concat(pieces, ignore_index=True) # concat of all names
grouped = names.groupby(["year","sex"])
top1000 = grouped.apply(get_top1000)
boys = top1000[top1000.sex=="M"]
girls = top1000[top1000.sex=="F"]
"""

table = top1000.pivot_table("prop",index="year",columns="sex",aggfunc=sum)
table.plot(
    title="Sum of table1000.prop by year and sex",
    xticks=range(1880,2020,10),
    yticks=np.linspace(0,1.2,13),
); # pylab.show()

### Note: seems like the top 1000 names have dropped off
### -changing times have changing popularity in names
### -ex: creating unique names

# # number of distinct names, high-to-low popularity
# # in top 50% births
boys2010df = boys[boys.year==2010]
# print boys2010df # [1000 rows x 5 columns] # sorted by .prop
# print boys2010df.sort_index()[:20]
# # Index([u'name', u'sex', u'births', u'year', u'prop'], dtype='object')
# print boys2010df.columns
# print boys2010df.index.name # None # index not set yet

# # numpy : vectorized approach
# # cumsum (cumulative sum) of "prop" col
# # searchsorted : returns position in cumsum,
# #                0.5 insert needed to keep in sorted order
# # --------------------------------------------------------
# # ref: http://beyondvalence.blogspot.com/2014/09/python-and-pandas-part-3-baby-names.html
# # .searchsorted(0.5) gets sorted index of 50th percent tile; returns 116
# # +1 --> 117 names consist of 50% of male births in 2010
boys2010prop_cumsum = boys2010df.sort_index(by="prop",ascending=False).prop.cumsum()
# # array is zero-indexed
# print boysprop_cumsum[:10] # printed by index (idx not set),

# # zero-indexed array, +1 to result gives 117
boys1900df = boys[boys.year==1900]
in1900 = boys1900df.sort_index(by="prop",ascending=False).prop.cumsum()
# # find indices where elements should be inserted to maintain order
# # :return indices: array of ints
# # .searchsorted(0.5) gets sorted index of 50th percent tile; returns 24 
# # +1 --> 25 names consist of 50% of male births in 1900
# print in1900.searchsorted(0.5)+1 # [25]
# print type(in1900) # <class 'pandas.core.series.Series'>

# # 
def get_quantile_count(group,q=0.5):
    group = group.sort_index(by="prop",ascending=False)
    return group.prop.cumsum().searchsorted(q)+1
diversity = (top1000.groupby(["year","sex"])
                    .apply(get_quantile_count))
diversity = diversity.unstack("sex")
# print diversity.head()
# print diversity.size, type(diversity)
# # 262 <class 'pandas.core.frame.DataFrame'>
# print diversity.empty # False

diversity.plot(
    title="Number of popular names in top 50%"
); pylab.show()
