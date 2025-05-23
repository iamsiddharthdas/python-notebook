'''

In Python, function arguments are the inputs that you can pass to a function when you call it.
They allow you to provide data to the function for it to work with.

'''

def sum(a,b):
    sum = a + b
    
    print('Sum: ',sum)
    
sum(1,2) # function call with two values


# Function argument with default values

def sum(a=7,b=8):
    sum = a + b
    
    print('Sum: ',sum)
    
sum(1,2) # function call with two values
sum(a=2) # function call with one value
sum() # function call with no value

# Python Keyword Argument
def display_info(first_name,last_name):
    print('First Name: ',first_name)
    print('Last Name: ',last_name)
    
display_info(last_name='Doe',first_name='John') # function call with keyword arguments

# Python with Arbitrary Arguments

def find_sum(*numbers):
    result = 0
    
    for num in numbers:
        result = result + num
    
    print("Sum: ",result)
    
find_sum(1,2,3) # function call with three values
find_sum(1,2,3,4,5) # function call with five values

