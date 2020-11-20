items = ['T-shirt', 'Sweater', 'Hoodie']

while True:
    command = input('Welcome to our shop, what do you want? (C,R,U,D): ')

    if command == 'C':
        items.append(input('Enter your new item here: '))

    elif command == 'U':
        for i in range(len(items)):
            print(f'{i+1}. {items[i]}')
        
        update_position = int(input('Enter position you want to update: ')) - 1
        if update_position < len(items):
            update_item = input('Enter new item: ')
            items[update_position] = update_item
        else:
            print('item not found')

    elif command == 'D':
        for i in range(len(items)):
            print(f'{i+1}. {items[i]}')

        delete_position = int(input('Enter position you want to delete: ')) - 1
        if delete_position < len(items):
            items.pop(delete_position)

    elif command == 'R':
        for i in range(len(items)):
            print(f'{i+1}. {items[i]}')

    else: 
        print('we dont do that here')
        break

    if command != 'R':
        for i in range(len(items)):
            print(f'{i+1}. {items[i]}')

