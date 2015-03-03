"""
np.loadtxt: load data into vanilla numpy arrays

np.genfromtxt: specialized load of np.loadtxt
               **more for structured arrays
"""

import numpy as np

arr=np.loadtxt("array_ex.txt",delimiter=",")
# array([
#     [ 0.580052,  0.18673 ,  1.040717,  1.134411],
#     [ 0.194163, -0.636917, -0.938659,  0.124094],
#     [-0.12641 ,  0.268607, -0.695724,  0.047428],
#     [-1.484413,  0.004176, -0.744203,  0.005487],
#     [ 2.302869,  0.200131,  1.670238, -1.88109 ],
#     [-0.19323 ,  1.047233,  0.482803,  0.960334]
# ])

newarr=np.append(arr,[11.,22.,33.,44.,55.])
# # note: this is saved as a 1D array
# #       newarr.reshape as needed
np.savetxt("array_ex_appendrow.txt",newarr)
np.loadtxt("array_ex_appendrow.txt")
