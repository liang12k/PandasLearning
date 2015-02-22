import numpy as np
from numpy.linalg import eigvals

"""
profiling code == determining where time is spent

cProfile: executes program, arbitrary code block
          while keeping track of time spent
          in each method
"""

def runLoop_linearAlgebra(niter=100):
    K=100
    results=[]
    for _ in xrange(niter):
        mat = np.random.randn(K,K)
        max_eigenvalue = np.abs(eigvals(mat)).max()
        results.append(max_eigenvalue)
    return results
some_results = runLoop_linearAlgebra()
print ("Largest one we saw was: %s" 
       % (np.max(some_results)))

# # %run ipythonbasics_profiling.py
# Largest one we saw was: 11.4336167842
