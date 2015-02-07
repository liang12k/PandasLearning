# # HISTOGRAMS

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

# # 1. histogram

# # Titanic_Age_pyplot-hist_noNAs
# pyplot.hist(titanic.Age.dropna()) # drop blank values in age; error if blank
# pylab.show()

# # Titanic_Age_pyplot-hist_noNAs-bins20
# pyplot.hist(titanic.Age.dropna(),bins=20); pylab.show()

# # Titanic_Age_distribplot-Hist_KDE
# sns.distplot(titanic.Age.dropna()); pylab.show()

# # Server_Time_hist-bins25_color
# pyplot.hist(server.Time, bins=25, color=sns.desaturate("indianred",1)); pylab.show()

# # Server_Time_distribplot-Hist_KDE
# sns.distplot(server.Time); pylab.show()

# # MLB_Salaries_hist-bins25
# pyplot.hist(mlb.Salary.dropna(), bins=25); pylab.show()

# # MLB_Salaries-distribplot-Hist_KDE
sns.distplot(mlb.Salary.dropna()); pylab.show()
