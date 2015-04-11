"""

"""

import pymongo
import requests
import json

# no such attribute 'Connection' (from the book)
# conn=pymongo.Connection("localhost",port=808080)
# from documentation:
# http://api.mongodb.org/python/current/tutorial.html
conn=pymongo.MongoClient("localhost",808080)
print conn
# MongoClient('localhost', 808080)
