import pandas
import numpy
import pylab

"""
 Groupby
 -using titanic.csv data
"""

titanic = pandas.read_csv("titanic.csv")
# print titanic.head()

# # descriptive statistics
# print titanic.describe()
"""
       PassengerId    Survived      Pclass         Age       SibSp  \
count   891.000000  891.000000  891.000000  714.000000  891.000000
mean    446.000000    0.383838    2.308642   29.699118    0.523008
std     257.353842    0.486592    0.836071   14.526497    1.102743
min       1.000000    0.000000    1.000000    0.420000    0.000000
25%     223.500000    0.000000    2.000000   20.125000    0.000000
50%     446.000000    0.000000    3.000000   28.000000    0.000000
75%     668.500000    1.000000    3.000000   38.000000    1.000000
max     891.000000    1.000000    3.000000   80.000000    8.000000

            Parch        Fare
count  891.000000  891.000000
mean     0.381594   32.204208
std      0.806057   49.693429
min      0.000000    0.000000
25%      0.000000    7.910400
50%      0.000000   14.454200
75%      0.000000   31.000000
max      6.000000  512.329200
"""

# # plot histogram
# titanic.Age.hist(); pylab.suptitle("Titanic - Age histogram"); pylab.show()

# # plot histogram with bins; default bins=10
# # -bins: the range per histogram bar to display
# # *Note: be wary of the bins range, distribute equal frequency (width) in bins 
# #        large+ == detail loss, broken "comby" look
# #        small+ == losing histogram doesn't portray data well, lose distribution sense
# titanic.Age.hist(bins=20); pylab.suptitle("Titanic - Age histogram"); pylab.show()

# # statistics: Age - men vs. women
sexgroup = titanic.groupby("Sex") # men, women genders with median Age
# print sexgroup.Age.median()
"""
Sex
female    27
male      29
Name: Age, dtype: float64
""" 

# print sexgroup.Age.describe() # descriptive stats of genders
"""
Sex
female  count    261.000000
        mean      27.915709
        std       14.110146
        min        0.750000
        25%       18.000000
        50%       27.000000
        75%       37.000000
        max       63.000000
male    count    453.000000
        mean      30.726645
        std       14.678201
        min        0.420000
        25%       21.000000
        50%       29.000000
        75%       39.000000
        max       80.000000
dtype: float64
"""

# # Age histogram
# sexgroup.get_group("male").Age.hist()
# pylab.suptitle("Titanic - Age.Male"); pylab.show()

# sexgroup.get_group("male").Age.hist(bins=20)
# pylab.suptitle("Titanic - Age.Male, bins=20"); pylab.show()

# # male, female histograms are overlayed; laid side by side
# sexgroup.get_group("male").Age.hist(bins=20)
# sexgroup.get_group("female").Age.hist(bins=20)
# pylab.suptitle("Titanic - Age.MaleFemale, bins=20"); pylab.show()

# # female median > male median
# # male max whisker ~ 65, with outliers (outliers explanation TBD)
sexgroup.boxplot(column="Age"); pylab.show()
