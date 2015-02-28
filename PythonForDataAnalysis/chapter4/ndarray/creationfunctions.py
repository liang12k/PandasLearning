#
# # np.zeros_like, np.ones_like
# from the ndarray, create zeros, ones array respectively
# based on the dimension of ndarray
# (same idea for .empty_like, an array of misc garbage values)
#
# # zeros_like
#
# >>> x
# array([[0, 1, 2],
#        [3, 4, 5]])
# >>> np.zeros_like(x)
# array([[0, 0, 0],
#        [0, 0, 0]])
#
# # ones_like
# >>> x
# array([[0, 1, 2],
#        [3, 4, 5]])
# >>> np.ones_like(x)
# array([[1, 1, 1],
#        [1, 1, 1]]);

#
# # np.asarray
# converts input (ex: list) into array
# if input is already array, nothing done
# can specify the dtype of array in args
# np.array(inpData, dtype=None)
#

#
# # np.arange
# to quickly create an array based on range of numbers
#
# >>> np.arange(3)
# array([0, 1, 2])
# >>> np.arange(3.0)
# array([ 0.,  1.,  2.])
# >>> np.arange(3,7)
# array([3, 4, 5, 6])
# >>> np.arange(3,7,2)
# array([3, 5])
#

#
# # np.eye
# get 2D array with ones on diagonal, zeros elsewhere
# numpy.eye(N, M=None, k=0, dtype=<type 'float'>)[source]
# http://docs.scipy.org/doc/numpy/reference/generated/numpy.eye.html
# N-rows, M-cols; k={1:"above",0:"on",-1:"below"}
# can set where ones diagonal positioned above,on,below diagonal based on 'k' arg
#

#
# # np.identity
# like np.eye, get identity square array
# diagonal is ones
# 
