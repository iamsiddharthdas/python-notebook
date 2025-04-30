'''
Return Function 
1. Breaks the function 
2. Prints the return value

Example:

def hello_func():
return 'hello Function'

print(hello_func())

-> prints hello Function
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
# Function with args and kwargs:
'''
Args and kwargs allow us to accept an arbitrary number of positional and keyword arguments in a function.

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
    
Positional arguments e.g. Maths, Science, English
Keyword arguments e.g. name, age, class, section

example:
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
student_info('Maths','Art', name='Sid', age=20)

->prints->  ('Maths', 'Art') -> tuple containing positional arguments
            {'name': 'Sid', 'age': 20} -> dictionary containing keyword arguments

Single star (*) is used to unpack the positional arguments into a tuple.
Double star (**) is used to unpack the keyword arguments into a dictionary.

# example:
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

course = ['Maths', 'Art']
info = {'name': 'Sid', 'age': 20}

student_info(course, info) 

# instead of passing the values individually, it passed the complete list and complete dictionary as a positional argument.
# prints (['Maths', 'Art'], {'name': 'Sid', 'age': 20}) 


student_info(*course, **info)   

# passes the values individually, 
# prints -> ('Maths', 'Art') -> unpacked the tuple
            {'name': 'Sid', 'age': 20} -> unpacked the dictionary   


'''

# Leap year and days in month

# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    ''' Returns True for leap years, False for non-leap years. '''
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    ''' Returns number of days in that month in that year. '''
    
    
    # year 2017 (example)
    # month 2 (February)
    if month < 1 or month > 12:
        return 'Invalid month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

is_leap(2020) # prints True
days_in_month(2017, 2) # prints 28


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

# Example usage:
print(prime_no(5))  # 5 is a prime number
print(prime_no(4))  # 4 is not a prime number

# The function table prints the multiplication table of a given number.

def table(num):
    for i in range(1, 11):
        print(num, 'x', i,'=', num * i)

table(12)

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
    choice = input("Enter 1 for square pattern, 2 for triangle pattern: ")

    if choice == '1':
        for i in range(5):
            for j in range(5):
                print("*", end=" ")
            print(end="\n")

    elif choice == '2':
        for i in range(5):
            print(' '*(5-i-1), end=' ')
            for j in range(i+1):
                print('*', end=' ')

            print(end='\n')

    else:
        print("Invalid input! Please enter 1 or 2.")


print_pattern()


# The function fibonacci_sequence generates the Fibonacci sequence up to the 5 terms.

def fibonacci_sequence(n):
    a = 0
    b = 1
    print(a)
    print(b)

    i = 1
    while i <= 5:
        c = a + b
        print(c)
        a = b
        b = c
        i += 1

fibonacci_sequence(6)


