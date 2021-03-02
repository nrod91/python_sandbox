# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
 # Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
#fruits2 = tuple(('Apples','Oranges','Grapes'))

# Single value needs trailing comma
fruits2 = ('Apples',)

# Get value
print(fruits[1])

# Can't change value
print[0] = 'Pears'

#print(fruits2,type(fruits2))

#print(fruits, fruits2) 



# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create a set
fruits_set = {'Apples','Oranges','Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# Clear set
fruits_set.clear()

print(fruits_set)

# Delete 
del fruits_set

print(fruits_set)
