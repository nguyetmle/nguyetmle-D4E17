from pymongo import MongoClient

client = MongoClient('localhost', 27017)

movie_database = client.get_database('mongo_practice')

movie_collection = movie_database.get_collection('movies')

# get all documents
print(movie_collection.find())

# get all docs with 'writer' set to 'quentin tarantino'
for x in movie_collection.find({},{'writer': 'Quentin Tarantino'}):
    print(x)

# # get all documents where actors include "Brad Pitt"
for x in movie_collection.find({}, {'actor': 'Brad Pitt'}):
    print(x)

# # get all documents with franchise set to "The Hobbit"
for x in movie_collection.find({'franchise': 'The Hobbit'}):
    print(x)

# get all movies released in the 90s
for x in movie_collection.find(
    {'year':
        {
            '$gt': 1990,
            '$lte': 2000
        }
    }
):
    print(x)

# get all movies released before the year 2000 or after 2010
for x in movie_collection.find(
    {
        '$or':
        [
            {'year': {'$lte': 2000}},
            {'year': {'$gt': 2010}}
        ]
    }
):
    print(x)


