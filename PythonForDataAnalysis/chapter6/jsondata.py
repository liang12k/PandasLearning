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
# # load JSON data as Python object
result=json.loads(obj); result
'''
{u'name': u'Wes',
 u'pet': None,
 u'places_lived': [u'United States', u'Spain', u'Germany'],
 u'siblings': [{u'age': 25, u'name': u'Scott', u'pet': u'Zuko'},
               {u'age': 33, u'name': u'Katie', u'pet': u'Cisco'}]}
'''
# # back into JSON
asjson=json.dumps(result); asjson
# '{"pet": null, "siblings": [{"pet": "Zuko", "age": 25, "name": "Scott"}, {"pet": "Cisco", "age": 33, "name": "Katie"}], "name": "Wes", "places_lived": ["United States", "Spain", "Germany"]}'

siblings=pd.DataFrame(
    result["siblings"],
    columns=["name","age","pet"]
)
siblings
'''
    name  age    pet
0  Scott   25   Zuko
1  Katie   33  Cisco
'''
rowidxs=["name","age","places_lived","pet"]
wesDf=pd.DataFrame(
    [result.get(idx) for idx in rowidxs],
    index=rowidxs,
    columns=["desc"]
).fillna("None given")
wesDf
'''
                                         desc
name                                      Wes
age                                None given
places_lived  [United States, Spain, Germany]
pet                                None given
'''
