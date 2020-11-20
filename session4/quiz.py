quiz = {
    'question': 'con chó có mấy chân?',
    'answer': 3,
    'choices': [
        '2 chân',
        '3 chân',
        '4 chân',
        '5 chân'
    ]
}

print(quiz['question'])
for i in range(len(quiz['choices'])):
    print(f'{i+1}. {quiz["choices"][i]}')
print()
answer = int(input('your answer? ')) 
if answer == quiz['answer']:
    print('congrats')
else:
    print('wrong, the correct answer is 3')



