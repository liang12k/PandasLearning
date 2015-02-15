import pandas
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
"""

"""
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
boysdf = boys[boys.year==2010]
# print boysdf # [1000 rows x 5 columns] # sorted by .prop
# print boysdf.sort_index()[:20]
# # Index([u'name', u'sex', u'births', u'year', u'prop'], dtype='object')
# print boysdf.columns
# print boysdf.index.name # None # index not set yet

# # numpy : vectorized approach
# # cumsum (cumulative sum) of "prop" col
# # searchsorted : returns position in cumsum,
# #                0.5 insert needed to keep in sorted order
boysprop_cumsum = boysdf.sort_index(by="prop",ascending=False).prop.cumsum()
print boysprop_cumsum[:10] # printed by index (idx not set),
