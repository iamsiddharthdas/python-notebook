'''
Return Function 
1. Breaks the function 
2. Prints the return value

Example:

def hello_func():
return 'hello Function'

print(hello_func())

-> prints hello Function

if don't pass any argument inside a function, it will give 'None' as output.

def fun():
    x=99
    
print(fun())

Output:
None

'''



# Modifying string in print statement:

'''
def hello_func():
    return 'Hello Function'

print(len('Test'))

-> prints 4 because the length of the string 'Test' is 4. So it does not print the return value of the function.

Using this concept, we can modify the function in the print statement to return the value we want to print.

def hello_func():
    return 'Hello Function'
print(hello_func().upper())

-> prints HELLO FUNCTION instead of Hello Function because we are using the upper() method to convert the string to uppercase.
'''

# Parameter and Argument:

'''
example:
def hello_func(greeting): # greeting is a parameter
    return '{} Function'.format(greeting)
    
print(hello_func('Hi')) 

-> prints Hi Function because we are passing 'Hi' as an argument to the function hello_func. 
The function takes the argument and returns 'Hi Function' by formatting the string with the value of greeting.

Default Parameter Value:

example:
def hello_func(greeting, name='You'): 
    # greeting & name are parameters with default value of name as 'You'
    # if name is not provided, it will take the default value 'You'
    return '{}, {}'.format(greeting, name)

print(hello_func('Hi'))

-> prints Hi, You 

Explanation: We are passing 'Hi' as an argument to the function hello_func. 
But we are not passing the second argument name, so it takes the default value 'You' and returns 'Hi, You'.


So when we pass the second argument name as 'Sid', it will override the default value of name.

example:
def hello_func(greeting, name='You'): 
    return '{}, {}'.format(greeting, name)

print(hello_func('Hi', 'Sid'))

-> prints Hi, Sid - because we are passing 'Hi' as an argument to the function hello_func and 'Sid' as the second argument.

'''


# Prime number checker
def prime_no(num):
    count = 0
    i = 1
    while i <= num:
        if num % i == 0:
            count += 1
        i += 1
    if count == 2:
        return f"{num} is a prime number"
    else:
        return f"{num} is not a prime number"
    
num = int(input(" Enter a number: "))
print(prime_no(num))

# Example usage:
# if u remove the input statement, then:

# print(prime_no(5))  -> 5 is a prime number
# print(prime_no(4))  -> 4 is not a prime number

# The function table prints the multiplication table of a given number.

def table():
    for i in range(1, 11):
        print(num, 'x', i,'=', num * i)

num = int(input("Enter a number to print its multiplication table: "))
table()


# The function find_lcm finds the least common multiple of three numbers.

def find_lcm(x, y, z):
    greater = max(x, y, z)

    while True:
        if greater % x == 0 and greater % y == 0 and greater % z == 0:
            return greater
        greater += 1


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

lcm = find_lcm(x, y, z)
print("LCM is", lcm)



# We dont have to necessarily use return in a function. We can use print inside the function and call the function.

# The function print_pattern prints a square or triangle pattern based on user input.

def print_pattern():
    
    n = int(input("Enter 1 for square pattern, 2 for triangle pattern: "))

    if n == 1:
        
        for i in range(5):
            for j in range(5):
                print("*", end=" ")
            print(end="\n")

    elif n == 2:
        
        for i in range(5):
            print(' '*(5-i-1), end=' ')
            for j in range(i+1):
                print('*', end=' ')
            print(end='\n')

    else:
        print("Invalid input! Please enter 1 or 2.")

print_pattern()


# The function fibonacci_sequence generates the Fibonacci sequence up to the 5 terms.

def fibonacci_sequence():
    n = int(input('Enter a num: '))
    
    a = 0
    b = 1
    print(a)
    print(b)

    i = 1
    while i <= n:
        c = a + b
        print(c)
        a = b
        b = c
        i += 1

fibonacci_sequence()


