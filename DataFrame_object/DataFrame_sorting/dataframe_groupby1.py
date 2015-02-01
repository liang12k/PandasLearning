import pandas
### # pylab is needed to render the plot window
import pylab

"""
'GroupBy' : splitting --> analyzing --> combining
 
Splitting:
 grouped obj : group of DataFrame objs in a dict-like structure

 ~~~ DataFrame --groupby--> grouped obj of DataFrames

Analyzing:
 can analyze the group of DataFrame objs

Combining:
 creating new data structures 
"""

mlb = pandas.read_csv("mlbsalaries.csv") # whole DataFrame
# print mlb # [19543 rows x 5 columns]
# print mlb.head()
# print mlb.tails()

### # Splitting
# dict of data by key "Year"
grpMlb = mlb.groupby("Year")
# print grpMlb # <pandas.core.groupby.DataFrameGroupBy object...>

'''
for k, group in grpMlb:
    print k
    print group
'''

### # Analysis
# generator comprehension
# each group -> sort by salary -> highest at top (ascending=False)
t = (group.sort_index(by="Salary", ascending=False)[:1] for yr, group in grpMlb)
# print t # <generator object <genexpr>...>

### # Combining
topsalaries = pandas.DataFrame()
for row in t:
    topsalaries = topsalaries.append(row)
# print topsalaries
# # sets index col to "Year", remove the left side of row index nums from list
# topsalaries = topsalaries.set_index(["Year"])
# print topsalaries

ts = topsalaries[["Year","Salary"]]
# print ts
ts = ts.set_index("Year")
# print ts

ts.plot(title="mlbsalaries_plot_SalaryByYear") 
### # need to install matplotlib, pylab 
# mlbsalaries_plot_SalaryByYear.png

### # pylab is needed to render the window; individually need to do show()
pylab.show()

grpMlb.Salary.median().plot(title="mlbsalaries_plot_SalaryByYear-Median") 
# == grpMlb["Salary"].median().plot()
# mlbsalaries_plot_SalaryByYear-Median.png

### # pylab is needed to render the window; individually need to do show()
pylab.show()
