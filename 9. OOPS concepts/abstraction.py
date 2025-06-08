'''
Abstraction:
Hiding the implementations details of a class and only showing the essential features to the user.

'''

# Example:

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self): 
        self.acc = True
        self.clutch = True
        print("Car started")

car1 = Car()
car1.start() # Automatic car start 

# Data abstraction

'''
@abstractmethod - its a decorator that isused to declare an abstract method in an abstract class
abstract method - body is not defined

'''

from abc import ABC, abstractmethod

class A(ABC): # class A inherits ABC

    @abstractmethod # decorator
    def dog(self): # abstract method
        pass

    @abstractmethod
    def cat(self): # abstract method
        pass

class B(A):

    def dog(self):
        print("Hello, I am dog")

    def cat(self):
        print("Hello, I am cat")

obj = B()
obj.dog()
obj.cat()

'''
Output:

Hello, I am dog
Hello, I am cat


'''
