#  nested conditional: one conditional that can be nested within another

salary = int(input('enter your salary (unit: million VND): '))
if salary > 100:
    print('buy car')
else: 
    if salary > 50:
        print('buy motorbike')
    else:
        print('buy bike')