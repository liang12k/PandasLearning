# # BOXPLOT

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

# # 2. Box plot

# # Titanic_Age_boxplot
# sns.boxplot(titanic.Age.dropna()); pylab.show()
# # Titanic_Age-groupbySex_boxplot
# sns.boxplot(titanic.Age, titanic.Sex, vert=False); pylab.show()

# # Server_Time_boxplot
# sns.boxplot(server.Time); pylab.show()

# # MLB_Salary_boxplot
# sns.boxplot(mlb.Salary); pylab.show()
