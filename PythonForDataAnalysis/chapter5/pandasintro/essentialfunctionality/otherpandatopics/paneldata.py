"""
Panel data structure
-3D analogue of DataFrame
-**note: N-dimension arrays unneccessary in many cases

.to_frame: converts panel to DataFrame
.to_panel: converts DataFrame to panel
"""

import numpy as np
from pandas import Series, DataFrame, Panel
import pandas.io.data as web

pdata=Panel(
    dict(
        (stk, web.get_data_yahoo(
                  stk,"1/1/2011", "6/1/2014")
     )for stk in ["AAPL","GOOG","MSFT","DELL"])
)
# pdata.to_frame().tail() # [2490 rows x 6 columns]
pdata
# indexes = date, cols = company ticker names
'''
<class 'pandas.core.panel.Panel'>
Dimensions: 4 (items) x 877 (major_axis) x 6 (minor_axis)
Items axis: AAPL to MSFT
Major_axis axis: 2011-01-03 00:00:00 to 2014-05-30 00:00:00
Minor_axis axis: Open to Adj Close
'''
pdata=pdata.swapaxes("items","minor")
pdata["Adj Close"].tail()
'''
             AAPL  DELL    GOOG   MSFT
Date
2014-05-23  86.58   NaN  552.70  39.34
2014-05-27  88.20   NaN  565.95  39.41
2014-05-28  87.97   NaN  561.68  39.23
2014-05-29  89.58   NaN  560.08  39.56
2014-05-30  89.24   NaN  559.89  40.15
'''
pdata.ix[:,"2013-02-15",:]
# select all data at specific date or
# range of dates
'''
Open    High     Low   Close    Volume  Adj Close
AAPL  468.85  470.16  459.92  460.16  97936300      62.92
DELL   13.70   13.83   13.68   13.81  20542600      13.57
GOOG     NaN     NaN     NaN     NaN       NaN        NaN
MSFT   28.04   28.16   27.88   28.01  49650900      26.28
'''
pdata.ix["Adj Close","2014-05-23":,:]
'''
             AAPL  DELL    GOOG   MSFT
Date
2014-05-23  86.58   NaN  552.70  39.34
2014-05-27  88.20   NaN  565.95  39.41
2014-05-28  87.97   NaN  561.68  39.23
2014-05-29  89.58   NaN  560.08  39.56
2014-05-30  89.24   NaN  559.89  40.15
'''
pdata.ix[["Close","Adj Close"],"11/15/2013",:]
'''
<class 'pandas.core.panel.Panel'>
Dimensions: 2 (items) x 134 (major_axis) x 4 (minor_axis)
Items axis: Closes to Adj Close
Major_axis axis: 2013-11-15 00:00:00 to 2014-05-30 00:00:00
Minor_axis axis: AAPL to MSFT
'''

# # 'stacked' DataFrame to represent panel data
# # -useful for statistical models
stacked=pdata.ix[:,"2014-05-25":,:].to_frame()
'''
                    Open    High     Low   Close     Volume  Adj Close
Date       minor
2014-05-27 AAPL   615.88  625.86  615.63  625.63   87216500      88.20
           GOOG   556.00  566.00  554.35  565.95    2098400     565.95
           MSFT    40.26   40.26   39.81   40.19   26160600      39.41
2014-05-28 AAPL   626.02  629.83  623.78  624.01   78870400      87.97
           GOOG   564.57  567.84  561.00  561.68    1647500     561.68
           MSFT    40.14   40.19   39.82   40.01   25711500      39.23
2014-05-29 AAPL   627.85  636.87  627.77  635.38   94118500      89.58
           GOOG   563.35  564.00  558.71  560.08    1350400     560.08
           MSFT    40.15   40.35   39.91   40.34   19888200      39.56
2014-05-30 AAPL   637.98  644.17  628.90  633.00  141005200      89.24
           GOOG   560.80  561.35  555.91  559.89    1766300     559.89
           MSFT    40.45   40.97   40.25   40.94   34567600      40.15
'''
