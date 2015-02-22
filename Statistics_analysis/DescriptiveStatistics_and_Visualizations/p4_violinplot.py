# # Violin Plot
# # -box plot + KDE

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

# # Violin Plot

# # Titanic_Age_violinplot
# sns.violinplot(titanic.Age.dropna()); pylab.show()

# # Titanic_Age-groupbySex_violinplot
# sns.violinplot(titanic.Age.dropna(), titanic.Sex); pylab.show()

# # MLB_Salaries_violinplot
sns.violinplot(mlb.Salary.dropna()); pylab.show()
