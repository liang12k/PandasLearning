"""
reductions (aka aggregations):
-called with array instance or np function

normal distribution (aka probability distribution)
-"Gaussian distribution"
>http://simple.wikipedia.org/wiki/Normal_distribution
: mean==location, std==scale
-best for large data population

standard normal distribution (aka z distribution)
-normal distribution w mean==0, variance==1
-bell curve design
"""

import numpy as np

arr=np.random.randn(5,4) # normal-distributed data
arr.mean() # == np.mean(arr)
arr.sum()
# can do individual row opers: arr[row_idx].sum()

# get single array of mean by:
arr.mean(axis=0 )  # col
arr.mean(axis=1 )  # row
arr.mean(axis=-1)  # last axis (in this case, 'x')
                   # note: y is the 1st (0th idx)

                   
