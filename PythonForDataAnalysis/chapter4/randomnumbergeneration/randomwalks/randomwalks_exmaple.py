"""
example - illustrative application of using array
          operations in simulation of random walks.
"""

import numpy as np
import matplotlib.pyplot as plt

# random walk starting at 0,
# steps of 1,-1 w equal probability

# thru python
import random
position=0
walk=[position]
steps=1000
for i in xrange(steps):
    step=1 if random.randint(0,1) else -1
    position += step
    walk.append(position)

# a=np.array(walk)
# plt.plot(a)
# plt.title("Random walk w +1/-1 steps")
# plt.savefig("ch4_randwalks")
# plt.show();

nsteps=1000
draws=np.random.randint(0,2,size=nsteps) # [0,2)
steps=np.where(draws>0,1,-1) # (cond, if-True, else)
walk=steps.cumsum() # array of steps by randn
# plt.plot(walk)
# plt.title("Random walk w +1/-1 steps")
# plt.savefig("ch4_randwalks_viaNumpy")
# plt.show()
walk.min(), walk.max()

# # first crossing time
# # -step when rand walk reaches particular value
#
# how long it took rand walk to get at least
# 10 steps away from origin 0 in either direction
# -abs (absolute value) as direction is negligible
# 
# bool array where walk exceeded 10
np.abs(walk)>=10
# specifically want to know index of the
# first occurence 10, -10 (either direction)
# -note: inefficient as it may scan entire array
(np.abs(walk)>=10).argmax()

# np.argmax : returns 1D array of indicies of max
#             arg; can specify axis to examine
# ex:
# arr=np.arange(12).reshape(4,3)
# np.argmax(arr) # 11
# # axis=0: cmp cols - only 3 cols
# np.argmax(arr,axis=0) # array([3, 3, 3])
# # axis=1: cmp rows - only 4 rows
# np.argmax(arr,axis=1) # array([2, 2, 2, 2])

# # simulating many rand walks at once
rwalks=5000
nsteps=1000
# size configures array shape to 5000x1000
draws=np.random.randint(0,2,size=(rwalks,nsteps))
steps=np.where(draws>0,1,-1)
walks=steps.cumsum(1) # cumsum by rows
walks.min(); walks.max()
# calculate min crossing time to 30 or -30
# **note: not all 5000 reach these numbers!
# -using np.any method gets bool array if cond met
hits30=(np.abs(walks)>=30).any(1) # any of the rows
hits30.sum() # total that hits 30 or -30
# using hits30 bool array as a 'filter' mask
# to take only rows that hit 30
# then .argmax gets the index where the hit happens
crossingtimes=(np.abs(walks[hits30])>=30).argmax(1)
crossingtimes.mean() # general index of hit


