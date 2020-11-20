from pymongo import MongoClient

client = MongoClient('localhost', 27017)

movie_database = client.get_database('mongo_practice')

movie_collection = movie_database.get_collection('movies')

# add a synopsis to "The Hobbit: An Unexpected Journey" : "A reluctant hobbit, Bilbo Baggins, sets out to the Lonely Mountain with a spirited group of dwarves to reclaim their mountain home - and the gold within it - from the dragon Smaug."
query_1 = {'title': 'The Hobbit: An Unexpected Journey'}
update_1 = {'$set':
    {
        'synopsis': 'A reluctant hobbit, Bilbo Baggins, sets out to the Lonely Mountain with a spirited group of dwarves to reclaim their mountain home - and the gold within it - from the dragon Smaug.'
    }
}
movie_collection.update_one(query_1, update_1)

# add a synopsis to "The Hobbit: The Desolation of Smaug" : "The dwarves, along with Bilbo Baggins and Gandalf the Grey, continue their quest to reclaim Erebor, their homeland, from Smaug. Bilbo Baggins is in possession of a mysterious and magical ring."
query_2 = {'title': 'The Hobbit: The Desolation of Smaug'}
update_2 = {
    '$set':
    {
        'sypnosis': 'The dwarves, along with Bilbo Baggins and Gandalf the Grey, continue their quest to reclaim Erebor, their homeland, from Smaug. Bilbo Baggins is in possession of a mysterious and magical ring.'
    }
}
movie_collection.update_one(query_2, update_2)

# add an actor named "Samuel L. Jackson" to the movie "Pulp Fiction"
query_3 = {'title': 'Pulp Fiction'}
update_3 = {
    '$push': {'actor': 'Samuel L. Jackson'}
}
movie_collection.update_one(query_3, update_3)

