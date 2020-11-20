from pymongo import MongoClient

client = MongoClient('localhost', 27017)

movie_database = client.get_database('mongo_practice')

movie_collection = movie_database.get_collection('movies')

# delete the movie "Pee Wee Herman's Big Adventure"
query_1 = {'title': "Pee Wee Herman's Big Adventure"}
movie_collection.delete_one(query_1)

# delete the movie "Avatar"
query_2 = {'title': 'Avatar'}
movie_collection.delete_one(query_2)



