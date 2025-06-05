'''

Other languages - Access modifier
Python - No access modifier, only naming convention

Public -> can be accessed outside a class
Private -> can be accessed within a class
Protected -> can be accessed within a class or inherited class

'''
class Person:
    __name = 'anonymous' # private variable (double underscore)
    
    def __hello():
        print("Hello")

p1 = Person()
print(p1.__name) # throws an error because __name is private variable
print(p1.__hello()) # throws an error because __hello is private method

# Can internal functions of the class access the private method?

class Person:
    __name = 'anonymous'
    
    def __hello(self):
        print("Hello person")
    def welcome(self):
        self.__hello() # call private method inside the welcome method

p1 = Person()
print(p1.welcome()) 
# private method called inside the welcome method which is not private. Hence it prints without error

'''
Output:
Hello person
None

Yes, the internal functions of the class can access the private method.
This is basically done to prevent exposing the instance attributes outside of the class.

'''
# How to keep the account password private in Account class? (example)

class Account:
    def __init__(self,acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # private (double underscore) -> __acc_pass
    
    def reset_pass(self):
        return self.__acc_pass # since this is defined inside the class, it will print
        
acc1 = Account("12345", "abcde")
print(acc1.acc_no)
# print(acc1.__acc_pass) # it won't print and will throw error coz it is private( cant be accessed oustide the class)
print(acc1.reset_pass()) # it will print, because it is defined inside the class

# Another example of private.
class A:
    __x = 100  # private variable (double underscore)
    y = 200
    
    def __init__(self):
        print("Hello i am A class constructor")
    def fun(self):
        print("Hello i am A class fun method")
        
obj = A()

print(obj.x) # Won't print coz it can't be accessed outside the class
print(obj.y)


# How to print obj.x ?

class A:
    __x = 100  # private (double underscore)
    y = 200
    
    def __init__(self):
        print("Hello i am A class constructor")
    def fun(self):
        print(self.__x) # accessing private variable
        print("Hello i am A class fun method")
        
obj = A()

print(obj.x) # Will print.
print(obj.y)

# How to access x from B class which is inherited?

class A:
    _x = 100  # protected (single underscore)
    y = 200
    
    def __init__(self):
        print("Hello i am A class constructor")
    def fun(self):
        print(self._x) 
        print("Hello i am A class fun method")
        
class B(A):
    a = 1500
    b = 1600
    
    def __int__(self):
        print(super()._x)
        
obj = B()

