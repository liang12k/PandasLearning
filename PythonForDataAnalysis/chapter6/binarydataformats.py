"""
pickle deserialization

"""

import pandas as pd

frame=pd.read_csv("ex1.csv"); print frame
'''
   a   b   c   d message
0  1   2   3   4   hello
1  5   6   7   8   world
2  9  10  11  12     foo
'''
# # .save is deprecated!
# frame.save("frame_pickle")
frame.to_pickle("ex1_frame_pickle")
print (pd.load("ex1_frame_pickle")
         .set_index(["message"]))
'''
         a   b   c   d
message
hello    1   2   3   4
world    5   6   7   8
foo      9  10  11  12
'''
