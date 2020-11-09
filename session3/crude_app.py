items = ['T-shirt', 'Sweater', 'Hoodie']

# C
items.append(input('Enter your new item here: '))

# R
for i in range(len(items)):
    print(f'{i+1}. {items[i]}')

# U
update_position = int(input('Enter position you want to update: ')) - 1
if update_position < len(items):
    update_item = input('Enter new item: ')
    items[update_position] = update_item
else:
    print('item not found')

#D
delete_position = int(input('Enter position you want to update: ')) - 1


