# # Cumulative Distribution Function
# # -cumulative curve based on KDE; easier to spot %s

import numpy
import pandas
from matplotlib import pyplot
import seaborn as sns # recommended standard
import pylab

sns.set_palette("deep", desat=.6)
sns.set_context(rc={"figure.figsize":(8,4)})

titanic = pandas.read_csv("titanic.csv"); # print titanic.head()
server = pandas.read_csv("serverdata.csv"); # print server.head()
mlb = pandas.read_csv("mlbsalaries.csv"); # print mlb.head()

# # Cumulative Distribution Function

# # p5_Titanic_Age_cumulDistrFunct
# # %s on y-axis, ages on x-axis
# sns.kdeplot(titanic.Age.dropna(),cumulative=True); pylab.show()

# # p5_Server_Time_cumulDistrFunct
# # %s on y-axis, milisec time  on x-axis
# sns.kdeplot(server.Time.dropna(), cumulative=True); pylab.show()

# # p5_MLB_Salary_cumulDistrFunct
# # %s on y-axis, salaries on x-axis
# sns.kdeplot(mlb.Salary.dropna(), cumulative=True); pylab.show()
