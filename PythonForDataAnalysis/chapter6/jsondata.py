"""
JSON: JavaScript Object Notation
-standard format for sending data by HTTP request
 between browsers and other applications
-flexible data format
-basic types: 
 objs (dicts), arrays (lists), strings, numbers,
 booleans, nulls

-**note: all keys in object must be strings!
"""

import json
import pandas as pd

obj="""
{
    "name":"Wes",
    "places_lived":[
        "United States",
        "Spain",
        "Germany"
    ],
    "pet":null,
    "siblings":[
        {"name":"Scott","age":25,"pet":"Zuko" },
        {"name":"Katie","age":33,"pet":"Cisco"}
    ],
}
"""
result=json.loads(obj); result
