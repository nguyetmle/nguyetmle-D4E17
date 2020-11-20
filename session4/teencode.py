teencode = {
    'dc': 'duoc',
    'vk': 'vo',
    'ck': 'chong'
}
while True:
    for key in teencode:
        print(key, end = ' ')
    print()
    print('*'*10)

    your_code = input('your code? ')
    if your_code in teencode:
        print('it means: ', teencode[your_code])
    else:
        choice = input('not found, do you want to contribute this word? (Y/N) ')
        if choice == 'Y':
            meaning = input('Enter your trans: ')
            teencode[your_code] = meaning
        else:
            print('thank you')
            break