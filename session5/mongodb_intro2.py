from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('localhost', 27017)

quiz_database = client.get_database('quiz')
quizzes_collection = quiz_database.get_collection('quizzes')

# query = {'_id': ObjectId("5fb3aeb0959d617f1957f51a")}
# update = {
#     '$push':{      # lệnh $push: thêm item
#         'choices': '5 tay'
#     }
# }

# quizzes_collection.update_one(query, update)

# update = {
#     '$pull':{      # lệnh $pull: xóa item
#         'choices': '5 tay'
#     }
# }

# quizzes_collection.update_one(query, update)

# query = {'date.day': 1}
# update = {
#     '$set': {
#         'date.month': 12
#     }
# }
# quizzes_collection.update_one(query,update)

# Delete items
query = {'date.day': 1}
quizzes_collection.delete_one(query)