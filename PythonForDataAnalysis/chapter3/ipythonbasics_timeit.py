import numpy as np

# # diffs: http://stackoverflow.com/questions/8619167/inconsistency-between-time-and-timeit-in-ipython
# # %time : runs statement once, reporting excution time
# # %timeit: temporarily turns off garbage collection during timing (default),
# #          run number of times (default n=1,000,000)
# #          ** more accurate b/c of numerous runs
# #
# # Wall time: start-to-completion task time
# #

strings = [
    'foo', 'foobar', 'baz', 
    'qux','python', 'Guido Van Rossum'
] * 100000
method1 = [x for x in strings if x.startswith('foo')] 
method2 = [x for x in strings if x[:3] == 'foo']

# # 
# # %timeit method1
# 10000000 loops, best of 3: 55.4 ns per loop
# 
# # %time method1
# CPU times: user 5 ms, sys: 2 ms, total: 7 ms
# Wall time: 11.9 ms  
#
# # %timieit method2
# 10000000 loops, best of 3: 47.8 ns per loop
# 
# # %time method2
# CPU times: user 5 ms, sys: 1 ms, total: 6 ms
# Wall time: 10 ms

xstr = "foobar"
ystr = "foo"
# #
# # %timeit xstr.startswith(ystr)
# 1000000 loops, best of 3: 416 ns per loop
#
# # %timeit xstr[:3] == ystr
# 10000000 loops, best of 3: 188 ns per loop
# 

