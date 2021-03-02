# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries


# create dict

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Use constructor
#person2 = dict(frist_name='Sara', last_name='Williams')

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'

print (person, type(person))

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())