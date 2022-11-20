"""
mongodb://agreco:<insertYourPassword>@docdb-2022-10-07-19-07-25.cluster-cl2rcpxusjn1.ap-south-1.docdb.amazonaws.com:27017/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false

mongodb://agreco:<insertYourPassword>@docdb-2022-10-07-19-07-25.cl2rcpxusjn1.ap-south-1.docdb.amazonaws.com:27017/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&retryWrites=false
"""
import pymongo
import datetime
import sys

##Create a MongoDB client, open a connection to Amazon DocumentDB as a replica set and specify the read preference as secondary preferred
client = pymongo.MongoClient(
    'mongodb://agreco:agreco123@localhost:27017/?ssl=false&readPreference=secondaryPreferred&retryWrites=false'
)

##Specify the database to be used
db = client.weather

##Specify the collection to be used
col = db.sample_collection

##Insert a single document
col.insert_one({'hello':'Amazon DocumentDB', "created_at": datetime.datetime.now()})

##Find the document that was previously written
x = col.find({'hello':'Amazon DocumentDB'})

##Print the result to the screen
print(x)

##Close the connection
client.close()
