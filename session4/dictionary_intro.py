person = {'name': 'Duc', 'yob': '96', 'job_title': 'dev'}
print(person)

"""
dictionary is a collection which is unordered, changeable, and indexed
{key: value}
"""

# Accessing Items: refer to key name
print(person['name']) 

for key in person:
    print(key)
    print(person[key])
    print(key, person[key])

# Adding Items
person['height'] = 175
print(person)

# Update Item: sửa value cho 1 key
person['height'] = 180
for key in person:
    print(key, person[key])

# Delete Items
del person['height'] # remove item with specified key name
print(person)

# Check if Key Exists: use the 'in' keyword
if 'name' in person:
    print('yes')