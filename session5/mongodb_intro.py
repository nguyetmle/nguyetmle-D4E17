from pymongo import MongoClient

client = MongoClient('localhost', 27017)

shopee_database = client.get_database('shopee')

product_collection = shopee_database.get_collection('products')

# data = list(product_collection.find()) # load all data into ram
# print(data[0]['name'])

# # có thể sử dụng for loop để lấy dữ liệu, khi ấy ko cần để data là kiểu list
# data = product_collection.find()  # get one data at time
# for d in data:
#     print(d)
#     print(d['name'])

# # queries (truy vấn): viết thông tin dữ liệu cần truy vấn trong bracket của find

# one_data = product_collection.find_one({'name': 'sp_2'}) # find record that has name sp_2
# print('only one', one_data)


# # Insert data
# insert_data = {
#     'name': 'sp_3',
#     'category': 'dsp_1',
#     'supplier': 'ncc_B'
# }
# product_collection.insert_one(insert_data)
# product_collection.insert_many([{},{}])

# Update data
query = {'name': 'sp_4'}
update = {
    '$set': {
        'name': 'sp_4',
        'price': '$40'
    }
}
product_collection.update_one(query, update)
