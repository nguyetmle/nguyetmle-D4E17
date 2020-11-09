# list: a collection which is ordered and changeable
# Create Read Update Delete

list_quan_ao = ['hoodie', 'ao phong', 'quan bo'] # trong list có thể chứa nhiều var types: str, int, float, boolean
print(list_quan_ao)
print(list_quan_ao[1]) # Read

# create
list_quan_ao.append('ao ba lo')  # (thêm lệnh append để add item vào list ở phía cuối cùng)
print(list_quan_ao)

"""
['a', 'b', 'c']:
    a, b, c: item
    index: vị trí của item, bắt đầu từ số 0 -> gọi dữ liệu trong list
    (đếm từ trái sang phải) index của a = 0, của b = 1, ...
    (đếm từ phải áng trái) index of last item = -1, index of second last item = -2,...
"""

len_list_quan_ao = len(list_quan_ao) # len: đếm dữ liệu trong list
for i in range(len_list_quan_ao):
    print('item', list_quan_ao[i])
    print('item', list_quan_ao[2])

# optimize 
for item in list_quan_ao: 
    print(item)

# update
list_quan_ao[2] = 'ao bo' # thay đổi biến : quan bo -> ao bo

# tìm index của 1 item trong list
index = list_quan_ao.index('hoodie')
print('index of hoodie is', index)

# delete 
remove_item_1 = list_quan_ao.pop(0) # delete item trong list dựa vào lệnh pop (điên index của item cần xóa)
print(remove_item_1)

remove_item_2 = list_quan_ao.remove('ao phong') # delete item by lệnh remove (điền item value)
print(remove_item_2)

# check item trong list
print('check item trong list', 'ao phong' in list_quan_ao) # boolean value: nếu có item trong list -> true, nếu ko có -> false

# range of indexes: you can specify a range of indexes by specifying where to start and where to end the range
this_list = ['apple', 'banana', 'kiwi', 'orange', 'mango', 'melon']
print(this_list[2:5]) # note: the item in position 5 is NOT included
print(this_list[:4]) # this example returns the items from the beginning to 'orange'
