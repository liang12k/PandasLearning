import pandas as pd
import numpy as pd
import pylab
from babynames_dataset1 import boys, top1000

# df = boys[boys.year==2010]
# prop_cumsum = df.sort_index(by="prop",ascending=False).prop.cumsum()

# df = boys[boys.year=1900]

def get_quantile_count(group,q=0.5):
    group=group.sort_index(by="prop",ascending=False)
    return group.prop.cumsum().searchsorted(q)+1
diversity = top1000.groupby(["year","sex"]).apply(get_quantile_count)
# diversity = diversity.unstack("sex")
diversity = diversity.unstack(0)
diversity.plot(); pylab.show()
