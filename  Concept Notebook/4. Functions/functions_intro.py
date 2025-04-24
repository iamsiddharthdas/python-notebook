
'''
Functions in Python

Functions are reusable blocks of code that perform a specific task. 
They help in organizing code, improving readability, and reducing redundancy. 
Functions can take inputs (arguments) and return outputs (results). 
In Python, functions are defined using the `def` keyword followed by the function name and parentheses.

'''

def addition():
    """
    This function takes two numbers as input and returns their sum.
    """
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    z = int(input("Enter third number: "))
    print(x + y + z)
    
def subtraction():
    """
    This function takes two numbers as input and returns their difference.
    """
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(x - y)

def multiplication():
    """
    This function takes two numbers as input and returns their product.
    """
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(x * y * z)
    
def division():
    """
    This function takes two numbers as input and returns their quotient.
    """
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(x / y)
    
def modulus():
    """
    This function takes two numbers as input and returns the remainder of their division.
    """
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(x % y)
    
def exponentiation():
    """
    This function takes two numbers as input and returns the result of raising the first number to the power of the second number.
    """
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(x ** y)
    
def floor_division():
    """
    This function takes two numbers as input and returns the result of floor division.
    """
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(x // y)

# Calculator function

def calculator():
    """
    This function provides a simple calculator interface to perform basic arithmetic operations.
    """
    print("Welcome to the calculator!")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Floor Division")
    
    choice = input("Enter your choice (1-7): ")
    
    if choice == '1':
        addition()
    elif choice == '2':
        subtraction()
    elif choice == '3':
        multiplication()
    elif choice == '4':
        division()
    elif choice == '5':
        modulus()
    elif choice == '6':
        exponentiation()
    elif choice == '7':
        floor_division()
    else:
        print("Invalid choice! Please try again.")

# Call the calculator function to start the program
calculator()



