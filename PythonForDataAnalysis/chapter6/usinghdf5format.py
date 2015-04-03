"""
HDF5: an option to write large data sets into
      binary format on disk

interfaces:
-PyTables: abstracts details to provide multiple
           flexible data container, table indexing,
           querying capability, support for some
           out-of-core computations
-h5py: direct, high-level interface to HDF5 api

HDF = hierarchical data format

each HDF5 file contains an internal file system-like
node structure enabling user to store multiple
datasets and supporting meta data

supports on-the-fly compression
-data with repeated patterns to be efficiently stored

good option to use for large datasets that don't
fit into memory
-efficiently read,write small sections of larger arrays
"""

import pandas as pd
from binarydataformats import frame

store=pd.HDFStore("mydata.h5")
store["obj"]=frame
store["obj1_col1"]=frame["a"]
print store["obj1"]
# output taken from book
# as of Apr-03-2015: having issues installing: pip install tables
# -clang error, can't detect HDF5 installation
'''
  a  b  c  d message 
0 1  2  3  4 hello 
1 5  6  7  8 world 
2 9 10 11 12 foo
'''
