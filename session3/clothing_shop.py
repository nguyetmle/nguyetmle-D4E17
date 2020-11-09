choice = input('welcome to our shop, what do you want? (C R U D)')

list_quan_ao = ['sweater', 'pant', 'hoodie']
if choice == 'C':
    for i in range(len(list_quan_ao)):
        print(list_quan_ao[i])
elif choice == 'U':
    choice_2 == input('what do you want to update?')
    for j in range(len(list_quan_ao)):
        list_quan_ao[j] = choice_2

    
   