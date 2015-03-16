"""

"""

import numpy as np
import pandas as pd
import pandas.io.data as web

alldata={}
for ticker in ["AAPL","IBM","MSFT","GOOG"]:
    alldata[ticker]=web.get_data_yahoo(
        ticker,"1/1/2010","1/1/2015"
    )
price=pd.DataFrame(
    {tic:data["Adj Close"]
     for tic,data in alldata.iteritems()}
) # [1258 rows x 3 columns]
volume=pd.DataFrame(
    {tic:data["Volume"]
     for tic,data in alldata.iteritems()}
) # [1258 rows x 3 columns]

