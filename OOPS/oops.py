'''
POP - Procedural Object Oriented Programming
|
function

OOPS - Object Oriented Programming System
|
class    
|
object

POP is suitable for simple, linear tasks — quick functions, scripts.
OOP is ideal for large, complex systems — apps, games, APIs.
Use functions in POP.
Use classes and objects in OOP to bundle data and behaviour.

POP:

def add(a, b):
    return a + b

result = add(5, 3)
print(result)

OOP:

class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()      # object
result = calc.add(5, 3)  # method call
print(result)

'''
# Example of OOPS using class 'Car'

class Car: #class
    engine = None # attributes
    tyres = None
    body = None
    color = None
    price = None
    
    def fun(self,a,b,c): # method with a,b,c as parameters
        print("Hi This Fun Method")
        
thar = Car() # object
creta = Car()


thar.fun(100,200,300) # method call
# thar.fun() is used for method call
# have to pass same number of parameters as defined in the method


thar.engine = "mHawk"
thar.tyres = "MRF"
thar.body = "Aluminium"
thar.color = "Red"
thar.price = 1200000

creta.engine = "TurboGDI"
creta.tyres = "CEAT"
creta.body = "Steel"
creta.color = "White"
creta.price = 2000000


print(thar.engine) # prints - mHawk
print(thar.tyres) # prints - MRF
print(thar.body) # prints - Aluminium
print(thar.color) # prints - Red
print(thar.price) # prints - 1200000

print(creta.engine) # prints - TurboGDI
print(creta.tyres) # prints - CEAT
print(creta.body) # prints - Steel
print(creta.color) # prints - White
print(creta.price) # prints - 2000000

'''
Class - CAR
Object - Thar, Creta
Attributes - Engine, Tyres, Body, Color, Price
Method - Fun

'''

# PRIME NUMBER CHECKER using OOP

class PrimeChecker:  # Class
    number = None    # Attribute

    def check_prime(self, num):  # Method
        self.number = num
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


num = int(input("Enter a number: "))


# result = PrimeChecker.check_prime(num)
'''
Why cant we do this?

Because, here we are calling an instance method (check_prime) directly 
on the class PrimeChecker without passing a self (object)
but instance methods require an instance of the class to work.

'''

checker = PrimeChecker() # Create an object


result = checker.check_prime(num) # Call the method using the object
print(result)
