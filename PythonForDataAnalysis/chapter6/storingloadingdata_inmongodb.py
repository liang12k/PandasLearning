"""

"""

import pymongo
import requests
import json
from interactingwith_htmlandwebapis import url

# no such attribute 'Connection' (from the book)
# conn=pymongo.Connection("localhost",port=808080)
# from documentation:
# http://api.mongodb.org/python/current/tutorial.html
conn=pymongo.MongoClient("localhost",808080)
print conn
# MongoClient('localhost', 808080)

coloradoBusinesses=conn.db.coloradoBusinesses
data=json.loads(requests.get(url).text)
[coloradoBusinesses.save(d) for d in data]
