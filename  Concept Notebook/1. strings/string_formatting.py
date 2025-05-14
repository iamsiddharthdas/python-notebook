greeting = 'Hello'
name = 'Michael'

'''
message = greeting + ', ' + name
print (message) #prints Hello, Michael

'''

msg1= '{}, {}. Welcome!'.format(greeting,name) # string formatting - placeholders {}
msg2= f'{greeting}, {name}. Welcome!' # f-strings - works in Python 3.6 or higher 
msg3= f'{greeting}, {name.upper()}. Welcome!' # f-strings - (can add attributes and methods like 'upper' on string variables)

print(msg1)
print(msg2)
print(msg3)



'''
print(dir(name)) -> to check all the attributes and methods that can be used with the string variable 'name'

print(help(str)) -> to check in detail all the attributes and methods on a string level
(detailed descriptions of what these methods do and what arguments they take)

'''

# F-strings: String Formatting in Python

'''

f-string is a way to format strings in Python. It allows you to embed expressions inside string literals, using curly braces {}.
It is evaluated at runtime and can contain any valid Python expression, including variables, arithmetic operations, and function calls.
It's more readable and concise than other string formatting methods, such as the format() method or the % operator.
They are also faster than other string formatting methods, as they are evaluated at runtime and do not require any additional function calls.
f-strings are available in Python 3.6 and later versions.

'''

y = 100

x = f'Value of y is {y}'
z = 'Value of y is y'

print(z) # prints Value of y is y
print(x) # prints Value of y is 100


# Example of f-string with attributes and methods

a = 'Apple'
b = 'Ball'
c = 'Cat'

print(f"a for {a}, b for {b}, c for {c}") # prints a for Apple, b for Ball, c for Cat
print(f"a for {a}, b for {b}, c for {c.upper()}") # prints a for Apple, b for Ball, c for CAT
print(f"a for {a}, b for {b}, c for {c.lower()}") # prints a for Apple, b for Ball, c for cat

# Printing multiplication table using f-strings

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}") # prints 5 x 1 = 5, 5 x 2 = 10, ..., 5 x 10 = 50
    
# Example of f-string with expressions
x = 10
y = 20
print(f"Sum of {x} and {y} is {x + y}") # prints Sum of 10 and 20 is 30

# Example of f-string with function calls
def square(n):
    return n * n
print(f"Square of {x} is {square(x)}") # prints Square of 10 is 100


# Longest string in Python

x=["Tomato","Brinjal","Okhra","Cabbage","Bottle Gourd","Cauliflower","Snake Gourd","Moringa"]

bigstring = " "

for i in range(len(x)):
    if len(bigstring) < len(x[i]):
        bigstring = bigstring
    else:
        bigstring = x[i]
        
print(bigstring) # prints the longest string in the list


# Using slicing to find the longest string in a list

x = ["Tomato", "Brinjal", "Okhra", "Cabbage", "Bottle Gourd", "Cauliflower", "Snake Gourd", "Moringa"]

longest = x[0]
for item in x[1:]:
    if len(item) > len(longest):
        longest = item

print(f"The longest vegetable name is: {longest}")



