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

# # **note: remove unnecessary commas from json
# #         dataset as it 's expecting another str
# #         key afterwards
# #  ie: ',' after 'siblings' list
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
    ]
}
"""
result=json.loads(obj); result
'''
{u'name': u'Wes',
 u'pet': None,
 u'places_lived': [u'United States', u'Spain', u'Germany'],
 u'siblings': [{u'age': 25, u'name': u'Scott', u'pet': u'Zuko'},
               {u'age': 33, u'name': u'Katie', u'pet': u'Cisco'}]}
'''
