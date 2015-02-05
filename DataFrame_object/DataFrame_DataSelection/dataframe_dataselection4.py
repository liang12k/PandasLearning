import pandas
import numpy
import pylab

statecrimes = pandas.read_csv("crime.csv")
# print statecrimes # [16422 rows x 5 columns]

# set row count limit
pandas.set_option("display.max_rows",10)
# print statecrimes # [16422 rows x 5 columns], 10 rows displayed

# statecrimes = statecrimes.set_index("State")
# print statecrimes

# 
cali_murdermanslaughter_Filter = (
    (statecrimes.State=="California")&
    (statecrimes.Crime=="Murder and nonnegligent Manslaughter")
)
calimmFilter = cali_murdermanslaughter_Filter

# print statecrimes[calimmFilter] # [46 rows x 5 columns]

caliCrime = statecrimes[calimmFilter]
caliCrime.plot(
    title="California - Murder and nonnegligent Manslaughter",
    x="Year", y="Count",
    legend=False, # defaults to show
)
pylab.show()
