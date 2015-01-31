import pandas

"""
DataFrame taking in csv
 -titanic.csv
"""

titanic = pandas.read_csv("titanic.csv")
# print titanic # too large to copy/paste; [891 rows x 12 columns]

# first 5 rows
# print titanic.head() # long table output

# last 5 rows
# print titanic.tail() # long table output

# get counts of col
print titanic.Sex.value_counts()
"""
male      577
female    314
dtype: int64
"""

print titanic.Survived.value_counts()
"""
0    549
1    342
dtype: int64
"""
