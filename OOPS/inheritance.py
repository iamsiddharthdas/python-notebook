
'''
Inheritance:
When a class inherits from another class, 
it inherits all the properties and methods of the parent class.
The child class can override the properties and methods of the parent class.
The child class can also add new properties and methods that are specific to its own class.

Parent class - Super Class
Child Class - Sub Class

Types of Inheritance:
1. Single Inheritance - The child class inherits from a single parent class
2. Multiple Inheritance - The child class inherits from multiple parent classes
3. Multilevel Inheritance - The child class inherits from a parent class, which in turn inherits from another parent class
4. Hierarchical Inheritance - The child class inherits from multiple parent classes, but each parent class has only one child class

'''

class Lion:
    x=100
    y=200
    
    def fun(self):
        print("Hello i am Lion class method")
        
        
class cub(Lion): # inheritance (cub class inherits from Lion class)
    a=1000
    b=2000
    
    def fun2(self):
        print("Hello i am cub class method")
        

obj=cub()

print(obj.x)
obj.fun() # calling the method of Lion class

obj.fun2() # calling the method of cub class



# Example of single inheritance and super class
class Lion:
    x=100
    y=200
    
    def __init__(self):
        print("hello i am Lion Class Constructor")
    
    def fun(self):
        print("Hello i am Lion class method")
        
        
class cub(Lion):
    a=1000
    b=2000
    def __init__(self):
        
        print("hello i am cub Class Constructor")
    
    def fun2(self):
        print(super().x) # super() is used to access the parent class but not modify it.
        print("Hello i am cub class method")
        
        
obj=cub() # obj calls the constructor of cub class
obj.x=1500

'''
Output:

hello i am cub Class Constructor

'''

# Overriding 

class Lion:
    x=100
    y=200
    
    def __init__(self):
        print("hello i am Lion Class Constructor")
    
    def fun(self):
        print("Hello i am Lion class method")
        
        
class cub(Lion):
    x=1000
    y=2000
    def __init__(self):
        print("hello i am cub Class Constructor")
    
    def fun(self):
        print("Hello i am cub class method")
        
        
obj=cub() # obj calls the constructor of cub class
obj.fun() # Method Overriding
print(obj.x) # Data Overriding

'''
Output:

hello i am cub Class Constructor      # From cub's __init__
Hello i am cub class method           # From cub's fun()
1000                                  # cub.x overrides Lion.x


'''

# Multilevel Inheritance

class Animal:
    x = 100
    y = 200
    def __init__(self):
        print("Hi i am animal constructor")

class Lion(Animal):
    a = 1000
    b = 2000
    def __init__(self):
        print("Hi i am Lion constructor")
        
class Cub(Lion):
    c = 1500
    d = 2500
    def __init__(self):
        print("Hi i am cub constructor")
        
obj = Cub() # obj calls the constructor of cub class
print(obj.c)
print(obj.a)
print(obj.x)

'''
Output:

Hi i am cub constructor
1500
1000
100

'''
# How to Print constructor for every class

class Animal:
    x=100
    y=200
    
    def __init__(self):
        print("Hi i am animal constructor")
        

class Lion(Animal):
    a=1000
    b=2000
    
    def __init__(self):
        super().__init__() # super() is used to call the constructor of parent class
        print("Hi i am Lion constructor")


class Cub(Lion):
    c=1500
    d=2500
    
    def __init__(self):
        super().__init__() # super() is used to call the constructor of parent class
        print("Hi i am Cub constructor")
        
        
obj=Cub()

print(obj.c)
print(obj.a)
print(obj.x)

# Multiple Inheritance

class A:
    x=100
    y=200
    
    def __init__(self):
        print("Hello i am A class constructor")
        
        
class B:
    x=1000
    y=2000
    
    def __init__(self):
        print("Hello i am B class constructor")


class C(A,B):
    x2 = 1500
    y2 = 2500
    def __init__(self):
        super().__init__() # super() is used to call the constructor of parent class of first priority i.e. A
        print("Hello i am C class constructor")
        
obj=C()

