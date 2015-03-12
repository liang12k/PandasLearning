"""

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
