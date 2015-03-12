"""
.applymap: apply function onto entire dataframe
-vs pd.Series' .map method (distinguish between each)
"""

import numpy as np
import pandas as pd

# # apply np ufuncs
# # refer to: Table4-3, 'Universal Functions'
frame=pd.DataFrame(
    np.random.randn(4,3),
    columns=list("bde"),
    index=["Utah","Ohio","Texas","Oregon"]
)
frame
#                b         d         e
# Utah   -1.415494  0.278801  0.586778
# Ohio    0.468205  0.658663 -0.911690
# Texas  -0.840659 -0.191017 -1.140930
# Oregon  1.007809  0.332413  0.467975
np.abs(frame)
#                b         d         e
# Utah    1.415494  0.278801  0.586778
# Ohio    0.468205  0.658663  0.911690
# Texas   0.840659  0.191017  1.140930
# Oregon  1.007809  0.332413  0.467975
#
# applying function on 1D arrays to
# each col and/or row using dataframe .apply
f=lambda x: x.max()-x.min()
frame.apply(f)
# see the original frame, not the .abs one
# for all values, get axis max-min
#
# for cols: axis=0 (default)
#
# b    2.423303
# d    0.849680
# e    1.727708
# dtype: float64
#
# for rows: axis=1
# Utah      2.002272
# Ohio      1.570353
# Texas     0.949913
# Oregon    0.675396
# dtype: float64

def f(x):
    return pd.Series(
               [x.min(),x.max()],
               index=["min","max"]
           )
#             b         d         e
# min -1.415494 -0.191017 -1.140930
# max  1.007809  0.658663  0.586778

# .applymap: map method to entire dataframe
# formatting string for each floating
# value in frame with 2 decimal precision
format=lambda x: "%.2f" % x
frame.applymap(format)
#             b      d      e
# Utah    -1.42   0.28   0.59
# Ohio     0.47   0.66  -0.91
# Texas   -0.84  -0.19  -1.14
# Oregon   1.01   0.33   0.47
