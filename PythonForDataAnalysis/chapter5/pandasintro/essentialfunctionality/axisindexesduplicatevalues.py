"""

"""

import numpy as np
import pandas as pd

obj=pd.Series(
    range(5),
    index=list("aabbc")
)
obj
# a    0
# a    1
# b    2
# b    3
# c    4
# dtype: int64
obj.index.is_unique
# False
# http://pandas.pydata.org/pandas-docs/dev/generated/pandas.Index.html
obj["a"]
# a    0
# a    1
# dtype: int64
obj["c"]
# 4

df=pd.DataFrame(
    np.random.randn(4,3),
    index=list("aabb")
)
df
#           0         1         2
# a -0.484903  1.393460  0.353473
# a -0.732426 -1.658375 -0.101024
# b  0.230659  0.230805 -1.237065
# b -0.355484  1.186528  0.465216
df.ix["b"]
#           0         1         2
# b  0.230659  0.230805 -1.237065
# b -0.355484  1.186528  0.465216
df.index.unique()
# array(['a', 'b'], dtype=object)
