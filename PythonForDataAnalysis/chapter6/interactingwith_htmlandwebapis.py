"""
requests: (package)
accessing websites' public APIs to get data feeds

response object: 
'text' attribute contains the content of GET query
**note: many web APIs return a JSON string the needs
        to be loaded into a Python object!
"""

import json
import pandas as pd
import requests

'''
# from the book, the following is out of date, 
# see below error message

url="http://search.twitter.com/search.json?q=python%20pandas"
resp=requests.get(url); print resp
# <Response [410]>

data=json.loads(resp.text)
print data.keys() # [u'errors']

NOTE:
-----
{"errors":[{"message":"The Twitter REST API v1 is no longer active. Please migrate to API v1.1. https://dev.twitter.com/docs/api/1.1/overview.","code":64}]}

# http://stackoverflow.com/questions/17207850/need-help-converting-to-twitter-api-v1-1-javascript
legacy twitter api - follow the steps in above link
**1.0 API is deprecated!
'''

# this sample .json page is saved in this dir too
url="http://data.colorado.gov/resource/4ykn-tg5h.json"
resp=requests.get(url); print resp
# <Response [200]>
data=json.loads(resp.text)
print data[0].keys()
'''
[u'principalzipcode',
 u'principalcity',
 u'agentprincipalcountry',
 u'entitytypeverbatim',
 u'agentprincipalzipcode',
 u'agentprincipalstate',
 u'entityname',
 u'entitytype',
 u'agentprincipaladdress1',
 u'agentfirstname',
 u'agentlastname',
 u'entitystatus',
 u'location',
 u'principalcountry',
 u'entityformdate',
 u'principaladdress1',
 u'agentprincipalcity',
 u'entityid',
 u'principalstate']
'''
coloradojson_fields=[
    "agentprincipalzipcode",
    "agentprincipaladdress1",
    "agentprincipalstate"
]
# # **note: pass in data as it is, a list
# #         because it has nested dicts,
# #         each dict is to be a row
# # http://stackoverflow.com/questions/26074447/creating-a-pandas-dataframe-from-a-dictionary
coloradobusinesses=pd.DataFrame(
    data,
    columns=coloradojson_fields,
)
print coloradobusinesses.head()
'''
  agentprincipalzipcode agentprincipaladdress1 agentprincipalstate
0            80513-8444   1617 White Water Ct.                  CO
1                 81301           777 Main Ave                  CO
2                 80236    3821 w greenwood pl                  CO
3                 80465    18707 S. Fairall Rd                  CO
4                 80022    7000 Glencoe Street                  CO
'''
print coloradobusinesses.ix[7]
# this is transposed for row 7
'''
agentprincipalzipcode             80135
agentprincipaladdress1    6800 N HWY 85
agentprincipalstate                  CO
Name: 7, dtype: object
'''
