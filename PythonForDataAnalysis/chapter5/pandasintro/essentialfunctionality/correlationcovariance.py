"""
correlation: 
-how closely related two sets of data are
-http://simple.wikipedia.org/wiki/Correlation

covariance: 
-measure of the strength of the correlation between two or more sets of random variates
-positive, negative, zero
-http://mathworld.wolfram.com/Covariance.html
-http://stats.stackexchange.com/questions/18058/how-would-you-explain-covariance-to-someone-who-understands-only-the-mean
-http://math.tutorvista.com/statistics/covariance.html
"""

import numpy as np
import pandas as pd
import pandas.io.data as web

alldata={}
for ticker in ["AAPL","IBM","MSFT","GOOG"]:
    alldata[ticker]=web.get_data_yahoo(
        ticker,"1/1/2010","1/1/2015"
    )
alldata["AAPL"].keys()
# Index([u'Open', u'High', u'Low', u'Close', u'Volume', u'Adj Close'], dtype='object')
price=pd.DataFrame(
    {tic:data["Adj Close"]
     for tic,data in alldata.iteritems()}
) # [1258 rows x 3 columns]
volume=pd.DataFrame(
    {tic:data["Volume"]
     for tic,data in alldata.iteritems()}
) # [1258 rows x 3 columns]

# compute changes in price
returns=price.pct_change()
returns.tail()
'''
                AAPL      GOOG       IBM      MSFT
Date
2014-12-24 -0.004728 -0.003430 -0.002607 -0.006444
2014-12-26  0.017657  0.009948  0.003236 -0.005439
2014-12-29 -0.000705 -0.006928 -0.011290 -0.009045
2014-12-30 -0.012163  0.000170 -0.002823 -0.008915
2014-12-31 -0.019004 -0.007579  0.002391 -0.012208
'''
returns.describe()
'''
              AAPL        GOOG          IBM         MSFT
count  1257.000000  193.000000  1257.000000  1257.000000
mean      0.001206   -0.000219     0.000297     0.000525
std       0.016784    0.013247     0.011683     0.013936
min      -0.123641   -0.046688    -0.082794    -0.114040
25%      -0.007499   -0.007579    -0.005516    -0.007447
50%       0.001042   -0.000154     0.000209     0.000000
75%       0.011088    0.008905     0.006470     0.008412
max       0.088742    0.037469     0.056653     0.072
'''
# # operating on specific datasets
#
# # get correlation
# # -relationship between 2 data sets
returns.MSFT.corr(returns.IBM)
# 0.49678917028603897
#
# # get covariance
# # -correlation relationship strength
returns.MSFT.cov(returns.IBM)
# 8.0883130640411769e-05

# # operating on entire DataFrame
# # -cov,corr returns full covariance,correlation
# # -**note: correlation betw self == 1, diagonal
returns.corr()
# 1.0 in diagonal, correlation to self
'''
          AAPL      GOOG       IBM      MSFT
AAPL  1.000000  0.323823  0.371235  0.345144
GOOG  0.323823  1.000000  0.316674  0.481007
IBM   0.371235  0.316674  1.000000  0.496789
MSFT  0.345144  0.481007  0.496789  1.000000
'''
returns.cov()
'''
          AAPL      GOOG       IBM      MSFT
AAPL  0.000282  0.000057  0.000073  0.000081
GOOG  0.000057  0.000175  0.000045  0.000072
IBM   0.000073  0.000045  0.000136  0.000081
MSFT  0.000081  0.000072  0.000081  0.000194
'''
# # .corrwith:
# # -correlations betw DataFrame's cols,rows
# #  w another Series or DataFrame
# # axis=1 gets correlation per row
#
# .corrwith for Series gets correlation value
# for each column (default)
returns.corrwith(returns.IBM)
# AAPL    0.371235
# GOOG    0.316674
# IBM     1.000000
# MSFT    0.496789
# dtype: float64
#
# .corrwith for DataFrame gets pct_change
returns.corrwith(volume)
# AAPL   -0.103036
# GOOG   -0.192948
# IBM    -0.189818
# MSFT   -0.098655
# dtype: float64
