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

'''

x=100

print(type(x),x)

x=float(x)

print(type(x),x)

prints <class 'float'> 100.0               

x=Lokesh
x=int(x)

print(x)

We get an error because we cannot convert a string to an integer

'''