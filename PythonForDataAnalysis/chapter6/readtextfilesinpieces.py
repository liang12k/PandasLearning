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

# # read a file in pieces using 'chunksize'
chunker=pd.read_csv("ex6.csv",chunksize=1000)
chunker
# <pandas.io.parsers.TextFileReader at 0x10bbe5fd0>
# # TextParser object:
# # -can be used to iterate over parts of file
# #  according to chunksize
tot=pd.Series([])
# for each piece, count the 'key' values
# fill NaN values with 0 to continue count
for piece in chunker:
    tot=tot.add(
        piece["key"].value_counts(),
        fill_value=0
    )
tot=tot.order(ascending=False); tot[:10]
'''
E    368
X    364
L    346
O    343
Q    340
M    338
J    337
F    335
K    334
H    330
dtype: float64
'''    
