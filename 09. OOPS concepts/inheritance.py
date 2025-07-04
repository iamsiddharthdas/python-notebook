
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
# Single inheritance

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

'''
super() is used to call the constructor of parent class
It is commonly used in multiple inheritance

'''

# Employee and Engineer class - Super() with single inheritance

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
        
    def showDetails(self):
        print("role = ", self.role)
        print("dept = ", self.dept)
        print("salary = ", self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__('ENGINEER', 'IT', '75,000') # super() is used to call the constructor of parent class

eng1 = Engineer('Elon',40)
eng1.showDetails()

'''
Output:

role =  ENGINEER
dept =  IT
salary =  75,000


'''

# Another example of single inheritance and super class

class Lion:
    x = 100
    y = 200

    def __init__(self):
        print("Hello, I am the Lion class constructor.")

    def fun(self):
        print("Hello, I am a method from the Lion class.")

class Cub(Lion):
    a = 1000
    b = 2000

    def __init__(self):
        super().__init__()  # Call the parent class constructor
        print("Hello, I am the Cub class constructor.")

    def fun2(self):
        print(super().x)  # Accessing class variable from parent
        super().fun()     # Calling parent method using super()
        print("Hello, I am a method from the Cub class.")


# Creating an object of Cub
obj = Cub()    # This will call both the Lion and Cub constructors
obj.fun2()     # This will demonstrate usage of super() in a method

'''
Output:

Hello, I am the Lion class constructor.     -> super().__init__()
Hello, I am the Cub class constructor.      -> __init__(self) of Cub
100                                         -> super().x
Hello, I am a method from the Lion class.   -> super().fun()
Hello, I am a method from the Cub class.    -> fun2(self)


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
