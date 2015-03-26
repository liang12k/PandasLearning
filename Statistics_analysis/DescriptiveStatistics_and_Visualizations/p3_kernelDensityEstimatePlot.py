# # KERNAL DENSITY ESTIMATE PLOT
# # -displays which values have a higher probability

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

# # KDE Plot (Kernel Density Plot)

# # Titanic_Age_kdeplot
# sns.kdeplot(titanic.Age.dropna(),shade=True); pylab.show()

# # Server_Time_kdeplot
# sns.kdeplot(server.Time.dropna(), shade=True); pylab.show()

# # MLB_Salary_kdeplot
sns.kdeplot(mlb.Salary.dropna(), shade=True); pylab.show()
