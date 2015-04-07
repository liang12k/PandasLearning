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

import urllib2
# from new twitter api
url=""
# resp=urllib2.urlopen(url); print resp
# data=json.loads(resp.text)
# print data.keys()
