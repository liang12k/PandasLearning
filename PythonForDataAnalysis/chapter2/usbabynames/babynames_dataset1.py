import pandas as pd
import pylab
import numpy as np

"""
US Baby Names 1880-2010
-----------------------
US Soc. Sec. Admin. (SSA) data on frequency of baby names
from 1880 through present (2010).

babynames_dataset1.py:
-loading csv files into DataFrames
-aggregate all files together into single merge DataFrame
-adding colname ("prop")
-quick sanity check on dataset based on "prop" col sum() to ~= 1
-get top 1000 of M,F names
"""

names1880 = pd.read_csv("names/yob1880.txt", names=["name","sex","births"])
# print names1880 # [2000 rows x 3 columns]
# # use sum of "births" col by sex, as total number of births in year 1880
# print names1880.groupby("sex").births.sum()

# # put all .txt files into a single DataFrame
years = range(1880,2011)
pieces = []
columns = ["name","sex","births"]
for year in years:
    path = "names/yob%d.txt" % (year)
    frame = pd.read_csv(path, names=columns)
    frame["year"] = year # # new col "year"
    pieces.append(frame) # # similar to qztable.vConcat list of DataFrames
# # concat every DataFrame into single whole DataFrame by row
# # ignore_index=True : ignores the original row num indexes from read_csv
names = pd.concat(pieces, ignore_index=True)
# print names # [1690784 rows x 4 columns]

# # aggregate data at year, sex using "groupby" or "pivot_table"
# # Note/Reminder: rows,cols is deprecated
total_births = names.pivot_table(
    "births", 
    index="year", # rows="year", 
    columns="sex", # cols="sex", 
    aggfunc=sum
)
# print total_births.tail()
# total_births.plot(title="Total births by sex and year"); pylab.show()

# # insert col "prop" == babies for each name / total number of births
# # prop val = 0.2; 2/100 babies w particular name
# # --group data by year & sex --> add new col to each group
def add_prop(group):
    births = group.births.astype(float) # int division floors
    group["prop"]=(births/births.sum()) # births of this group / total births
    return group
names = names.groupby(["year","sex"]).apply(add_prop)
# print names # [1690784 rows x 5 columns]

# # self-code: see top,bottom 5 of "names" DataFrame 
# #            based on gender, sorted by "prop" col
# m_names = names[names.sex=="M"]
# f_names = names[names.sex=="F"]
# gethead_prop = lambda dF: dF.sort(columns=["prop"]).head()
# gettail_prop = lambda dF: dF.sort(columns=["prop"]).tail()
# 
# print names[names.sex=="M"].sort(columns=["prop"]).head()
# print names[names.sex=="M"].sort(columns=["prop"]).tail()
# print names[names.sex=="F"].sort(columns=["prop"]).head()
# print names[names.sex=="F"].sort(columns=["prop"]).tail()
# # 

# # sanity check (verify "prop" col sum == 1 within all groups)
# # np.allclose check that group sums ~= 1 (doesn't need to be exact!)
# print np.allclose(names.groupby(["year","sex"]).prop.sum(), 1) # True

# # extract data subset to analyze top 1000 names for each
# # (sex / year) combination using group operation
# # ::: separate DataFrames by "year","sex"; ordered by "births" count
def get_top1000(group):
    return group.sort_index(by="births",ascending=False)[:1000]
grouped = names.groupby(["year","sex"])
top1000 = grouped.apply(get_top1000)
# print top1000

# # working w top 1000 names dataset
# # pivot_table made DataFrame have:
# # :index = "year" (per row)
# # :columns = "names"
# # :values = "births" count per name in year 
boys = top1000[top1000.sex=="M"]
girls = top1000[top1000.sex=="F"]
total_births = top1000.pivot_table(
    "births", index="year", columns="name", aggfunc="sum"
)# using args "index","columns" because "rows","cols" are deprecated
# print total_births

# # taking multiple subset of 4 colnames
# # plots count of 4 names in births in years range
subset = total_births[["John","Harry","Mary","Marilyn"]]
# subset.plot(
#     subplots=True, figsize=(12,10), grid=False, 
#     title="Number of births per year"
# ); pylab.show()

### Note: seems like the 4 names have dropped off
### -changing times have changing popularity in names
### -ex: creating unique names

# # big spike in 1960
kennysubset = total_births["Kenny"]
# kennysubset.plot(
#     subplots=True, grid=True, title="Kenny: Number of births per year"
# ); # pylab.show()
