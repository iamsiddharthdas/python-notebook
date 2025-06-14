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

'''


# @staticmethod

'''

Static Method:

For every new instance or object, this method wont be created repeatedly.
It will be created only once and it can be used by all the objects of the class.
Static method doesnt modify or access instance attributes. So its generally used for utility.
e.g. class car -> start(), stop()


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


# @classmethod

'''

@staticmethod can't access or modify class attributes.
So, @classmethod is used to access or modify class attributes.

A class method is bound to class and receives the class(cls) as an implicit first argument.


'''

class Person:
    name = 'anonymous'
    
    # def changeName(self,name):
    #     Person.name = name 
    #     # self.__class__.name = name (works the same as Person.name)
    
    @classmethod # decorator
    def changeName(cls,name): 
        cls.name = name 
        # Now changes will happen on the class level, not on the object level.

p1 = Person()
p1.changeName('Sid')
print(p1.name) # prints Sid
print(Person.name) # prints Sid

'''
instance method (self) - can access or modify instance attributes.
class method (cls) - can access or modify class attributes.
static method - cannot access or modify either instance or class attributes.

'''

# @property

'''
We use @property decorator on any method in the class to use the method as a property.

'''

class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.maths = math
        self.percentage = str((self.phy + self.chem + self.maths) / 3) + '%'
        
std1 = Student(98,97,99)
print(std1.percentage) # prints 98%

'''
When rechecked, teacher found that the physics marks was incorrect for student 1.

'''
std1.phy = 86 # changed the physics marks
print(std1.phy) # prints 86 
print(std1.percentage) # still prints 98% which is incorrect

'''
This happens because self.percentage takes the initial set value of 
self.phy, self.chem and self.maths for percentage calculations. Not the updated values.

To avoid this, we use @property decorator.

'''

class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.maths = math
        self.percentage = str((self.phy + self.chem + self.maths) / 3) + '%'
        
    # def calcPercentage(self):
    #     self.percentage = str((self.phy + self.chem + self.maths) / 3) + '%' (works same as @property decorator)
    
    @property # decorator 
    def percentage(self):
        return str((self.phy + self.chem + self.maths) / 3) + '%'
    

std1 = Student(98,97,99)
print(std1.percentage) # prints 98%

std1.phy = 86 # changed the physics marks
print(std1.phy) # prints 86 
print(std1.percentage) # prints updated percentage i.e. 94%

