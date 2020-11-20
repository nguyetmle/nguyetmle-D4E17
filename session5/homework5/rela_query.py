from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('localhost', 27017)

relationship_database = client.get_database('relationships')

user_collection = relationship_database.get_collection('users')
post_collection = relationship_database.get_collection('posts')
comment_collection = relationship_database.get_collection('comments')

# find all users
user_collection.find()

# find all posts
post_collection.find()

# find all posts that was authored by 'GoodGuyGreg"
for x in post_collection.find({'username': 'GoodGuyGreg'}):
    print(x)

# find all posts that was authored by "ScumbagSteve"
for x in post_collection.find({'username': 'ScumbagSteve'}):
    print(x)

# find all comments
comment_collection.find()

# find all comments that was authored by "GoodGuyGreg"
for x in comment_collection.find({'username': 'GoodGuyGreg'}):
    print(x)

# find all comments that was authored by "ScumbagSteve"
for x in comment_collection.find({'username': "ScumbagSteve"}):
    print(x)

# find all comments belonging to the post "Reports a bug in your code
for x in comment_collection.find({'post': ObjectId("5fb7a248c918d07b4b8174a1")}):
    print(x)

