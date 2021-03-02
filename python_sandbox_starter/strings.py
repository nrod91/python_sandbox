# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = "Nick"
age = 37

# Concatenate
print('Concatenate: Hello, my name is ' + name + ' and I am ' + str(age) )

# String Formatting

# Arguments by position
print('Arguements by postion: My name is {name} and I am {age}'.format(name=name, age=age))

#F-Strings (3.6+)
print(f'F-strings: Hello, my name is {name} and I am {age}')

# String Methods
s = 'hello world'

# Captialize String
print(s.capitalize())

# Make all lower
print(s.upper())

# Swap case
print(s.swapcase)

# Get length
print(len(s))

# Replace
print(s.replace('world','everyone'))

# Count
sub = 'h'
print(s.count(sub))