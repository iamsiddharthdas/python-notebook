'''
Decorators: Allow us to wrap another function in order to 
extend the behaviour of the wrapped function without permanently modifying it.

Manual decorator:

def make_pretty(func):
    def inner():
        print("Hi i am Decorator")
        func()
        print("Bye")
    return inner
    
@make_pretty  # decorator
def ordinary():
    print("I am ordinary")
    
ordinary()

Output:

Hi i am Decorator
I am ordinary
Bye

---

def outer_function(func):
    def inner_function(*args):
        print("Hello Good Eveing")
        func(*args)
        print("Good Night")
        
    return inner_function


@outer_function
def real_function(*args):
    print("My Args values Are",args)
    
    
real_function(10,20,30,40,50,60,70,80)


Types of Decorators:
1. Class Decorator -> decorates a class e.g. @classmethod
2. Method Decorator -> decorates a method e.g. @staticmethod

Static Method:
Methods that dont use the self parameter (work at class level)

Why static methods are used?
They can be called without creating an object of the class


'''

# static method

class Student:
    @staticmethod # decorator
    def college():
        print('ABC College')
        
Student.college()

'''
Output:
ABC College

'''
# static method in single inheritance

class Car:
    color = 'Red'
    @staticmethod # decorator
    def start():
        return "Car started"
    @staticmethod # decorator
    def stop():
        return "Car stopped"
        
class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name
        
car1 = ToyotaCar('Fortuner')
car2 = ToyotaCar('Innova')

print(car1.start()) # prints Car started
print(car1.name) # prints Fortuner
print(car1.color) # prints Red
print(car1.stop()) # prints Car stopped

print(car2.start()) # prints Car started
print(car2.name) # prints Innova
print(car2.color) # prints Red
print(car2.stop()) # prints Car stopped

# static method in multiple inheritance

class Car:
    @staticmethod # decorator
    def start():
        return "Car started"
    @staticmethod # decorator
    def stop():
        return "Car stopped"
        
class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand
        
class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type
        
car1 = Fortuner('diesel')
print(car1.start())

'''
Output:
Car started

'''

# Data abstraction

from abc import ABC, abstractmethod

class A(ABC):

    @abstractmethod
    def dog(self):
        pass

    @abstractmethod
    def cat(self):
        pass

class B(A):

    def dog(self):
        print("Hello, I am dog")

    def cat(self):
        print("Hello, I am cat")

obj = B()
obj.dog()
obj.cat()