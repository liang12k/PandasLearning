"""
going thru small chunks of large dataset
-ie: test a little first
"""

import pandas as pd

result=pd.read_csv("ex6.csv"); result
# [10000 rows x 5 columns]
result.columns
# Index([u'one', u'two', u'three', u'four', u'key'], dtype='object')
pd.read_csv("ex6.csv",nrows=5)
'''
        one       two     three      four key
0  0.467976 -0.038649 -0.295344 -1.824726   L
1 -0.358893  1.404453  0.704965 -0.200638   B
2 -0.501840  0.659254 -0.421691 -0.057688   G
3  0.204886  1.074134  1.388361 -0.982404   R
4  0.354628 -0.133116  0.283763 -0.837063   Q
'''
