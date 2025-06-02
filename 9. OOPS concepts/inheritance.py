
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
    x1=150
    y1=250

    def __init__(self):
        print("Hello i am B class constructor")

class C():
    x2=1500
    y2=2500

    def __init__(self):
        super().__init__()
        print("Hello i am C class constructor")

class D(C,A,B):
    x3=1000
    y3=2000

    def __init__(self):
        super().__init__()
        print("Hello I am D class constructor")

obj=D()

print(obj.x)
print(obj.x1)
print(obj.x2)
print(obj.x3)

# Hierarchichal inheritance. 

class A:
    x=100
    y=200

    def __init__(self):
        print("Hello i am A class constructor")

class B(A):
    x1=150
    y1=250

    def __init__(self):
        print("Hello i am B class constructor")

class C(A):
    x2=1500
    y2=2500

    def __init__(self):
        super().__init__()
        print("Hello i am C class constructor")

class D(A):
    x3=1000
    y3=2000

    def __init__(self):
        super().__init__()
        print("Hello I am D class constructor")


obj=B()
obj1=C()
obj2=D()

print(obj.x)
print(obj.x1)
print(obj1.x2)
print(obj2.x3)


# Hybrid Inheritance.

class A:
    x=100
    y=200

    def __init__(self):
        print("Hello i am A class constructor")

class B(A):
    x1=150
    y1=250

    def __init__(self):
        print("Hello i am B class constructor")

class C(A):
    x2=1500
    y2=2500

    def __init__(self):
        super().__init__()
        print("Hello i am C class constructor")

class D(C,B):
    x3=1000
    y3=2000

    def __init__(self):
        super().__init__()
        print("Hello I am D class constructor")

class E(C,D):
    x4=1600
    y4=2600
    
    def __init__(self):
        super().__init__()
        print("Hello I am class E constructor")


obj=E()

print(obj.x)
print(obj.x1)
print(obj.x2)
print(obj.x3)
print(obj.x4)


# 2nd example of hybrid inheritance:

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Subclasses using hierarchical inheritance
class Mammal(Animal):
    def give_birth(self):
        return f"{self.name} is giving birth to live young."

class Bird(Animal):
    def lay_eggs(self):
        return f"{self.name} is laying eggs."

# Derived class using multiple inheritance
class Platypus(Mammal, Bird):
    def speak(self):
        return f"{self.name} says Quack!"

# Example usage
platypus_obj = Platypus("Perry")

print(platypus_obj.speak())        # Output: Perry says Quack!
print(platypus_obj.give_birth())   # Output: Perry is giving birth to live young.
print(platypus_obj.lay_eggs())     # Output: Perry is laying eggs.
