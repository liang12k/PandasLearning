"""
arrays saved as uncompressed raw binary format
with .npy extension as default using np.save

multiple arrays in zip archive using np.savez
as format.npz; loaded as a 'dict' format w keys
"""

import numpy as np

samplefname="arange10"
arr=np.arange(10)
# np.save(samplefname,arr) # defaults to '.npy' ext
# np.load(samplefname+".npy")
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# # .load of .npz is a 'dict' format
# # user assigns keynames
brr=np.arange(12).reshape(4,3)
np.savez(samplefname+"_archive.npz",a=arr,b=brr)
np.load( samplefname+"_archive.npz")
# <numpy.lib.npyio.NpzFile at 0x11026e990>
#
# get array by the 'key' name
np.load(samplefname+"_archive.npz")["a"]
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np.load(samplefname+"_archive.npz")["b"]
# array([
#     [ 0,  1,  2],
#     [ 3,  4,  5],
#     [ 6,  7,  8],
#     [ 9, 10, 11]
# ])

