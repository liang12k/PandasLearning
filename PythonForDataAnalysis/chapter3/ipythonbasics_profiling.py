import numpy as np
from numpy.linalg import eigvals

"""
profiling code == determining where time is spent

in python-
cProfile: executes program, arbitrary code block
          while keeping track of time spent
          in each method

------------------------
generally-
%prun _method_()

using output 'filtering'
: <#>: replace w a number, total lines output displayed
: <s_key>: sort by key, 
: ref: http://ipython.org/ipython-doc/2/api/generated/IPython.core.magics.execution.html
:          Note: can chain sorts by -s ___ -s ___ ...
%prun -l <#> -s <s_key> _method_()
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
#

# %prun ipythonbasics_profiling.py
# 
# similar to terminal cmd (reg. shell):
# >>> python -m cProfile -s cumulative ipythonbasics_profiling.py
# 
# # %prun -l 7 -s cumulative ipythonbasics_profiling.py
# # -l : set a limit of output
# # -s : sort profile by given key
# # cumulative : key, cumulative time
#
# 
# 4003 function calls in 1.367 seconds
# 
#    Ordered by: cumulative time
#    List reduced from 32 to 7 due to restriction
# 


