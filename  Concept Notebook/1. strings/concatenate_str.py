greeting = 'Hello'
name= 'Michael'

'''
message = greeting + ', ' + name
print (message) #prints Hello, Michael

'''

msg1= '{}, {}. Welcome!'.format(greeting. name) # string formatting - placeholders {}
msg2= f'{greeting}, {name}. Welcome!' # f-strings - works in Python 3.6 or higher 
msg3= f'{greeting}, {name.upper}. Welcome!' # f-strings - (can add attributes and methods like 'upper' on string variables)


'''
print(dir(name)) -> to check all the attributes and methods that can be used with the string variable 'name'

print(help(str)) -> to check in detail all the attributes and methods on a string level
(detailed descriptions of what these methods do and what arguments they take)

'''

