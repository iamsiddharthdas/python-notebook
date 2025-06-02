'''

Other languages - Access modifier
Python - No access modifier, only naming convention

Private -> within a class
Protected -> within a class or inherited class

'''

class A:
    __x = 100  # private variable
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

