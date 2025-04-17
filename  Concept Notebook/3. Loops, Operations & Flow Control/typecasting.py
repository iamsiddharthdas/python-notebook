'''
Typecasting is the process of converting a variable from one type to another.
Implicit typecasting is done automatically by Python when it is required.
Explicit typecasting is done by the user using the built-in functions.
The built-in functions for typecasting are:
int() - converts a value to an integer
float() - converts a value to a float
str() - converts a value to a string
bool() - converts a value to a boolean
list() - converts a value to a list
tuple() - converts a value to a tuple
set() - converts a value to a set
dict() - converts a value to a dictionary

Example:
x = 10
y = 20.5
z = "30"
a = True
b = [1, 2, 3]
c = (4, 5, 6)
d = {7: "seven", 8: "eight"}
print(int(y)) # prints 20
print(float(x)) # prints 10.0
print(str(x)) # prints "10"
print(bool(x)) # prints True
print(list(x)) # prints [10]
print(tuple(x)) # prints (10,)
print(set(x)) # prints {10}
print(dict(x)) # prints {10: 10}


# Example of implicit typecasting
x = 10
y = 20.5
z = x + y # x is implicitly converted to float
print(z) # prints 30.5

# Example of explicit typecasting
x = 10
y = 20.5
z = int(y) # y is explicitly converted to int
print(z) # prints 20

'''

# Explicit typecasting (more examples)

x = 100
x = float(x)
print(type(x),x)
# prints <class 'float'> 100.0 

x='Lokesh'
x=int(x)
print(x)
# We get an error because we cannot convert a string to an integer

y='1000'
y=int(y)
print(y)
# it prints 1000 because if the string has integer, python is smart enough to detect that.
# it will print 1000.0 if we write y=float(y)

z='1000L'
z=int(z)
print(z)
# We get an error because addition of the alphabet 'L' makes it a string. Hence, can't be converted to integer.
# Note: String will either read it as Integer or Float or string literal itself. Cant be mixed.

value = input('Whats the value? ')
print(type(value))
# input can be float, int or even boolean
# But whatever value you input, the output will be <class 'str'>

# So, to fix that, we need this
value1 = int(input('Whats the value? ')) 
print(type(value1))# prints <class 'int'>

value2 = float(input('Whats the value? '))
print(type(value2))# prints <class 'float'>

value3 = str(input('Whats the value? '))
print(type(value3))# prints <class 'str'>

value4 = bool(input('Whats the value? '))
print(type(value4))# prints <class 'bool'>