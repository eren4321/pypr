import pymongo
from pymongo import MongoClient
import io
import json

connection = MongoClient('localhost', 27017)
db = connection.mydatabase
collection = db.hurriyet
a = db.hurriyet.find().limit(10).sort([("retweet", pymongo.DESCENDING)])

b = []
# for follower in a.sort('follower_count',pymongo.DESCENDING) :
# print(follower)
# for favorite in a.sort('favorite',pymongo.DESCENDING) :
# print(favorite)
for retweet in a:
    b.append(retweet)


with io.open('hurriyet.json', 'w', encoding="utf-8") as f:
    for item in b:

        item["_id"] = str(item["_id"])
        item["created"] = ""
        item["tarih"]  =""

        print(item)
        f.write("%s\n" % json.dumps(item))
    f.close()

connection = MongoClient('localhost', 27017)
db = connection.mydatabase
collection = db.milliyet
a = db.milliyet.find().limit(10).sort([("retweet", pymongo.DESCENDING)])

b = []
# for follower in a.sort('follower_count',pymongo.DESCENDING) :
# print(follower)
# for favorite in a.sort('favorite',pymongo.DESCENDING) :
# print(favorite)
for retweet in a:
    b.append(retweet)


with io.open('milliyet.json', 'w', encoding="utf-8") as f:
    for item in b:

        item["_id"] = str(item["_id"])
        item["created"] = ""
        item["tarih"]  =""

        print(item)
        f.write("%s\n" % json.dumps(item))
    f.close()



connection = MongoClient('localhost', 27017)
db = connection.mydatabase
collection = db.cnn
a = db.cnn.find().limit(10).sort([("retweet", pymongo.DESCENDING)])

b = []
# for follower in a.sort('follower_count',pymongo.DESCENDING) :
# print(follower)
# for favorite in a.sort('favorite',pymongo.DESCENDING) :
# print(favorite)
for retweet in a:
    b.append(retweet)


with io.open('cnn.json', 'w', encoding="utf-8") as f:
    for item in b:

        item["_id"] = str(item["_id"])
        item["created"] = ""
        item["tarih"]  =""

        print(item)
        f.write("%s\n" % json.dumps(item))
    f.close()



connection = MongoClient('localhost', 27017)
db = connection.mydatabase
collection = db.kanald
a = db.kanald.find().limit(10).sort([("retweet", pymongo.DESCENDING)])

b = []
# for follower in a.sort('follower_count',pymongo.DESCENDING) :
# print(follower)
# for favorite in a.sort('favorite',pymongo.DESCENDING) :
# print(favorite)
for retweet in a:
    b.append(retweet)


with io.open('kanald.json', 'w', encoding="utf-8") as f:
    for item in b:

        item["_id"] = str(item["_id"])
        item["created"] = ""
        item["tarih"]  =""

        print(item)
        f.write("%s\n" % json.dumps(item))
    f.close()

