sheep_sizes = [5, 7, 300, 90, 24, 50, 75]
print('Hello, my name is Hiep and these are my sheep sizes')
print(sheep_sizes)

for j in range(1,4):
    print(f'month {j}')
    max_sheep = max(sheep_sizes)
    print(f'Now my biggest sheep has size {max_sheep} lets shear it')

    sheep_remove = int(sheep_sizes.index(max_sheep))
    sheep_sizes[sheep_remove] = 8
    print('After shearing, here is my flock')
    print(sheep_sizes)

    for i in range(len(sheep_sizes)):
        sheep_sizes[i] += 50
    print('One month has passed, now here is my flock')
    print(sheep_sizes)
    print(end= '\n')

print('My flock has size in total:', sum(sheep_sizes))
money = int(sum(sheep_sizes)) * 2 
print(f'I would get {sum(sheep_sizes)} * 2$ = {money}$')




