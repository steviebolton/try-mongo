import pymongo


MONGODB_URI = "mongodb://root:horses22@ds259361.mlab.com:59361/mytestdb"

DB_NAME = "mytestdb"

COLLECTION_NAME = "myFirstMDB"


import pymongo



try:
    conn = pymongo.MongoClient(MONGODB_URI)
    print("Mongo is connected!")
except pymongo.errors.ConnectionFailure as e:
    print("Could not connect to MongoDB: %s") % e
    
coll = conn[DB_NAME][COLLECTION_NAME]

documents = coll.find()

for doc in documents:
    print(doc)