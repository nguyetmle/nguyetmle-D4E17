from pymongo import MongoClient

client = MongoClient('localhost', 27017)
quiz_database = client.get_database('quiz')
quizzes_collection = quiz_database.get_collection('quizzes')

quizzes = [
    {
        'question': 'Con cò có mấy chân?',
        'awnser': 3,
        'choices': [
            '2 chân',
            '3 chân',
            '1 chân',
            '4 chân'
        ]
    },
    {
        'question': 'Con mèo có mấy chân?',
        'awnser': 2,
        'choices': [
            '1 chân',
            '3 chân',
            '2 chân',
            '4 chân'
        ]
    }
]

# insert data vào mongoDB
# C1: 
# quizzes_collection.insert_many(quizzes)

# C2:
for quizz in quizzes:
    quizzes_collection.insert_one(quizz)
   

