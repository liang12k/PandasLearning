"""

"""

import numpy as np

x=np.arange(1,7).reshape(2,3).astype(float)
y=np.array([[6.,23.],[-1,7],[8,9]])

x
# array([
#     [ 1.,  2.,  3.],
#     [ 4.,  5.,  6.]
# ])
y
# array([
#     [  6.,  23.],
#     [ -1.,   7.],
#     [  8.,   9.]
# ])

# # matrix dot product
x.dot(y)
# array([
#     [  28.,   64.],
#     [  67.,  181.]
# ])
#
# # explanation of dot product
#
# [
#     [[x11*y11 + x12*y12 + x13*y13],[x11*y21 + x12*y22 + x13*y23]]
#     [[x21*y11 + x22*y12 + x23*y13],[x21*y21 + x22*y22+ x23*y23]]
# ]
# 
# ||
# \/
# 
# [
#     [[1*6 + 2*-1 + 3*8],[1*23 + 2*7 + 3*9]],
#     [[4*6 + 5*-1 + 6*8],[4*23 + 5*7 + 6*9]]
# ]

# # 2D dot 1D == 1D result
# # note: same lengths for dot product
#
np.dot(x,np.ones(3)) # array([  6.,  15.])

# # np.linalg
from numpy.linalg import inv, qr

X=np.random.randn(5,5)
# array([
#     [-0.66706974, -1.25832611,  0.00665293,  0.02006916, -0.65824227],
#     [ 1.35723034,  1.09107502, -0.47777076,  2.62102802,  1.03389214],
#     [-0.22688536,  2.4728362 ,  0.63903981,  0.69843976,  0.37672321],
#     [-0.80396399,  0.36054707, -1.39229984,  0.47861955, -0.77891109],
#     [ 0.24133964,  0.03257192,  0.97260588, -0.74530087,  0.01482598]
# ])
#
# # X.T transposes X's rows <--> cols
#
mat=X.T.dot(X)
# array([
#     [ 3.04313612,  1.4771751 ,  0.55621557,  2.82082195,  2.38664487],
#     [ 1.4771751 ,  9.01980328,  0.58027549,  4.70990075,  2.60756092],
#     [ 0.55621557,  0.58027549,  3.52114208, -2.19705214,  0.84129608],
#     [ 2.82082195,  4.70990075, -2.19705214,  8.14255883,  2.57591648],
#     [ 2.38664487,  2.60756092,  0.84129608,  2.57591648,  2.25105852]
# ])
#
# # computes multiplicative inverse of matrix
#
inv(mat)
# array([
#     [  5.5853928 ,   1.28771956,   0.56520529,  -0.18056862, -7.41807972],
#     [  1.28771956,   0.49329974,   0.03008723,  -0.167849  , -1.75587868],
#     [  0.56520529,   0.03008723,   0.8866508 ,   0.51953664, -1.55998496],
#     [ -0.18056862,  -0.167849  ,   0.51953664,   0.5673888 , -0.45756279],
#     [ -7.41807972,  -1.75587868,  -1.55998496,  -0.45756279,  11.4496958 ]
# ])
#
# # get an 'identity', diagonal 1s
# # http://mathworld.wolfram.com/MatrixInverse.html
# 
mat.dot(inv(mat))
# array([
#     [  1.00000000e+00,  -8.88178420e-16,   0.00000000e+00, 0.00000000e+00,   0.00000000e+00],
#     [  0.00000000e+00,   1.00000000e+00,   0.00000000e+00, 2.22044605e-16,  -3.55271368e-15],
#     [  0.00000000e+00,   0.00000000e+00,   1.00000000e+00, 2.22044605e-16,  -1.77635684e-15],
#     [  3.55271368e-15,   0.00000000e+00,  -8.88178420e-16, 1.00000000e+00,  -3.55271368e-15],
#     [  3.55271368e-15,  -4.44089210e-16,   0.00000000e+00, 0.00000000e+00,   1.00000000e+00]
# ])
# 
# # get qr factorization of matrix
# # :graham-schmidt process
# # -http://goo.gl/TIqO5n
# # -factor a matrix as a product of 2 matrices Q,R
# #
# # [Q,R] = qr(A,0)
# #         A is a mxn matrix,
# #         Q is mxn orthogonal,
# #         R is nxn upper triangular
#
# # **TODO** -- understand QR factorization
q,r=qr(mat)
# this output should have:
# q=[q1,q2,q3....] # q.T.dot(q) == I; identity
# r is an upper triangular, all 0s below
# r=[
#     [#, #, #, ...],
#     [0, #, #, ...],
#     [0, 0, #, ...],
# ]

# # numpy.linalg funcs
# 
# diag - Return the diagonal (or off-diagonal)
         # elements of a square matrix as a 1D array,
         # or convert a 1D array into a square matrix
         # with zeros on the off-diagonal
# dot - Matrix multiplication
# trace - get the sum of the diagonal elements
# det - get the matrix determinant
# eig - get the eigenvalues and eigenvectors
        # of a square matrix
# inv - get the inverse of a square matrix
# pinv - get the Moore-Penrose pseudo-inverse
        # inverse of a square matrix qr Compute the
        # QR decomposition
# svd - get the singular value decomposition (SVD)
# solve - Solve the linear system Ax = b for x,
        # where A is a square matrix
# lstsq - get the least-squares solution to y = Xb