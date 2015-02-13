import pandas as pd
import pylab

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
