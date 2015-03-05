"""
np.random > random (python) in speed

pseudorandom number generator (PNGR)
-relies on a 'seed'
 this seed state holds the same 'random' values
 for random generation
 :: seed the random generator w a fixed value
-http://stackoverflow.com/questions/5836335/consistenly-create-same-random-numpy-array
-http://en.wikipedia.org/wiki/Pseudorandom_number_generator

note: np.random.seed ~= global variable
      not thread-safe
      -http://stackoverflow.com/questions/7029993/differences-between-numpy-random-and-random-random-in-python
      np.random.RandomState() is a better option
      w many RandomState attrs
      -http://docs.scipy.org/doc/numpy/reference/generated/numpy.random.RandomState.html
"""

import numpy as np

np.set_printoptions(precision=4)

samples=np.random.normal(size=(4,4))
# array([
#     [-0.5167, -0.8497, -0.1321, -1.6618],
#     [-0.2247,  0.1668, -0.0352,  1.3548],
#     [-1.3641,  0.4263, -0.2719,  0.8427],
#     [ 0.3167,  0.0219, -2.5457,  0.8528]
# ])

from random import normalvariate
# N=1000000
# %timeit samples=[normalvariate(0,1) for _ in xrange(N)]
# 1 loops, best of 3: 1.75 s per loop

# %timeit np.random.norma(size=N)
# 10 loops, best of 3: 71.7 ms per loop

# # Table 4-8
# seed - seed the random number generator
#        fixed 'random' numbers
#
# permutation - return random permutation of a
#               sequence or return a permuted range
#
# rand - samples from uniform distribution
#
# randint - random integers from given
#           low-to-high range, and size
#
# randn - samples from normal distribution w mean 0
#         and std deviation 1 (MATLAB-like interface)
#
# binomial - samples from binomial distribution of n
#            w range [0,1], all numbers between [0,n]
#
# normal - samples from normal (Gaussian) distribution
#
# beta - samples from beta distribution
#        : case of Dirichlet distribution
#
# chisquare - samples from chi-square distribution
#             : statistical significance tests
#             
# gamma - samples from gamma distribution
#         : two param real numbers family of
#           continuous probability distributions
#         
# uniform - sample from uniform [0,1) distribution
#           : rectangular distribution
#           : continous = measured, constant probability within a range
#           : discrete = counted, only certain values
#
