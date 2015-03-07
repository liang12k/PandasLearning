"""
DataFrame: tabular, spreadsheet-like data structure
           containing ordered collection of cols
           ^ each col can be diff val (~qztable.Schema)
           has row,col index
           kind of dict of Series (sharing same idx)
           ** data stored as 1D or 2D blocks
"""

import numpy as np
import pandas as pd

# most common DataFrame creation is using
# dict of equal-sized lists or np.array
data={
    "state":["Ohio"]*3+["Nevada"]*2,
    "year":[2000,2001,2002,2001,2002],
    "pop":[1.5,1.7,3.6,2.4,2.9]
}
frame=pd.DataFrame(data)
frame
   # pop   state  year
   # 0  1.5    Ohio  2000
   # 1  1.7    Ohio  2001
   # 2  3.6    Ohio  2002
   # 3  2.4  Nevada  2001
   # 4  2.9  Nevada  2002

   
