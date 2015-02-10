##### ### # Using json
import json

path = "usagov_bitly_data2012-03-16-1331923249.txt"
# print open(path).readline()

# # list comprehension; json loads collection of strings
records = [json.loads(line) for line in open(path)]
# print records[0]

# print records[0]["tz"] # America/New_York


##### ### # Counting Time Zones
# time_zones = [rec["tz"] for rec in records] # KeyError "tz"; use dict.get()
time_zones = [rec["tz"] for rec in records if "tz" in rec]
# print time_zones[:10]

# # note: include rec in list if "tz", not just rec.get("tz") for every rec
# time_zones = [rec.get("tz") for rec in records if rec.get("tz")]

# # long way, using dict
def get_counts(sequence):
    counts = {}
    ### # original; one-lined the if-else 4 lines into 2
    for x in sequence:
        if x in counts: counts[x] += 1
        else: counts[x] = 1
    
    ### # shortened the for-loop to create the dict 'counts'
    # # note: this doesn't work! counts was never filled w values; 
    # #       will always be 1 for all keys
    # counts = dict((x,counts.get(x,0)+1) for x in sequence)
    
    return counts
# counts = get_counts(time_zones); print counts; print counts["America/New_York"]

def get_counts2(sequence):
    from collections import defaultdict
    counts = defaultdict(int) # values initialized to 0
    for x in sequence: counts[x] += 1
    return counts
counts = get_counts2(time_zones);
# print counts; print counts["America/New_York"]
# print len(time_zones) # 3440

# # top 10 time zones & their counts
def top_counts(count_dict, n=10):
    # 2-tuples : [(k,v),...]
    # dict.items() gets a list; returns 2-tuples
    # dict.iteritems() gets a iterator-generator; yields 2-tuples
    value_key_pairs = [(count,tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
# print top_counts(counts)

# https://docs.python.org/2/library/collections.html#collections.Counter
# counting hashable objs; dict mapping, keywd args, string (per elem)
from collections import Counter
counts = Counter(time_zones)
# print counts.most_common(10)

##### ### # Counting time zones with pandas
from pandas import DataFrame, Series
import pandas as pd

frame = DataFrame(records)
# print frame # [3560 rows x 18 columns], summary view
tz_counts = frame["tz"].value_counts()
# print tz_counts[:10]

# # fill in substitute value for unknown, missing time zone data
# .fillna replace NA/empty strings in zone col
clean_tz = frame["tz"].fillna("Missing") 
# blank times get "Unknown" zone name
clean_tz[clean_tz==""]="Unknown"
tz_counts = clean_tz.value_counts()
# print tz_counts[:10]

# # plot using matplotlib
import pylab
# tz_counts[:10].plot(kind="barh",rot=0,title="Time-Zones Top10"); pylab.show()

# # investigating field; 
# # frame = DataFrame(records)
# print frame["a"][1]
# print frame["a"][50]
# print frame["a"][51]

# # .dropna : remove blanks
results = Series([x.split()[0] for x in frame.a.dropna()])
# print results[:5]

# # decompose top time-zones into (non-)Windows
# # remove missing agents
import numpy as np
cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe["a"].str.contains("Windows"),"Windows","Not Windows")
# print operating_system[:5]

# # groupby data by time-zone col & new list of operating systems
by_tz_os = cframe.groupby(["tz", operating_system])
# print by_tz_os # <pandas.core.groupby.DataFrameGroupBy object...>
# # get (size) --> shape into table (unstack) --> fill blanks w 0 (fillna)
agg_counts = by_tz_os.size().unstack().fillna(0)
# print agg_counts[:10]

# # select top overall time zones
# # construct indirect index array from agg_counts row counts
# # sort in ascending order
# # http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.sum.html
# # sum col '1', argsort value & omitting NA/null values
indexer = agg_counts.sum(1).argsort()
# print indexer[:10]

# # take : select rows in [indexer] order, slice off last 10 rows
count_subset = agg_counts.take(indexer)[-10:]
# print count_subset

# # bar plot; stacked bar plot (stacked=True)
# count_subset.plot(kind="barh",stacked=True,title="Windows/Not Windows - top10")
# pylab.show()

# # normalize rows to sum to 1; replot, better to see relative %s
# # range of [0.0,1.0] view of %s
# # http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.div.html
# # .div : divide arrays, define axis
normed_subset = count_subset.div(count_subset.sum(1),axis=0)
# normed_subset.plot(kind="barh",stacked=True,title="Windows/Not Windows - NormalizedSum==1")
# pylab.show()

