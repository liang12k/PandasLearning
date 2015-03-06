"""
example - illustrative application of using array
          operations in simulation of random walks.
"""

import numpy as np
import matplotlib.pyplot as plt

# random walk starting at 0,
# steps of 1,-1 w equal probability
#
# thru python
import random
position=0
walk=[position]
steps=1000
for i in xrange(steps):
    step=1 if random.randint(0,1) else -1
    position += step
    walk.append(position)

