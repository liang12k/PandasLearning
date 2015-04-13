"""
to get mongodb working, be sure to install mongodb!
follow instructions here:
http://docs.mongodb.org/manual/tutorial/install-mongodb-on-os-x/

**note: mongodb is running in root '/' folder /data/db/
  ex: initandlisten] ERROR:   addr already in use
^ the db.0, .ns, .lock files are created there
"""

import pandas as pd
import pymongo
import requests
import json
from interactingwith_htmlandwebapis import url

# no such attribute 'Connection' (from the book)
# conn=pymongo.Connection("localhost",port=808080)
# from documentation:
# http://api.mongodb.org/python/current/tutorial.html
conn=pymongo.MongoClient()
print conn.test_database
# Database(MongoClient('localhost', 27017), u'test_database')

coloradoBusinesses=conn.db.coloradoBusinesses
data=json.loads(requests.get(url).text)
[coloradoBusinesses.save(d) for d in data]

cursor=coloradoBusinesses.find(
    {
        "agentprincipalzipcode":"81303"
    }
)
coBusin_fields=[
    "agentfirstname",
    "agentlastname",
    "agentprincipalcity",
    "agentprincipaladdress1",
    "agentprincipalzipcode"
]
result=pd.DataFrame(
    list(cursor),
    columns=coBusin_fields
)
'''
  agentfirstname agentlastname agentprincipalcity  agentprincipaladdress1  \
0           Rani          Holt            Durango  250 Morning Glory Lane
1           Rani          Holt            Durango  250 Morning Glory Lane
2           Rani          Holt            Durango  250 Morning Glory Lane
3           Rani          Holt            Durango  250 Morning Glory Lane
4           Rani          Holt            Durango  250 Morning Glory Lane

  agentprincipalzipcode
0                 81303
1                 81303
2                 81303
3                 81303
4                 81303
'''
