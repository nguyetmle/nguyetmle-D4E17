n = int(input('enter n = '))
for row in range(1, n+1):
    for col in range(1, n+1):
        if col % 2 == 0 and row % 2 == 1:
            print('0', end = ' ')
        elif col % 2 == 0 and row % 2 == 0:
            print('1', end = ' ')
        elif col % 2 == 1 and row % 2 == 0:
            print('0', end = ' ')
        else: 
            print('1', end = ' ')
    print()

