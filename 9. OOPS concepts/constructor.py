'''
Constructor in OOPS:

__init__ function - All classes have a function called __init__(), which is always executed when the class is being initiated.
Even if we don't write this fucntion, the __init  function is automatically created by python.

Properties:
1. It is used to initialize the object's state and perform any necessary setup operations.
2. In Python, constructors are defined using the __init__ method.
3. Constructor always takes an argument 'self'. 
(The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.)
4. return statement cannot be used in __init__ method, except None. 

Default constructor example:

class abc:
    x=100
    y=200
    def __init__(self): # take no argument
        print("Hello I am abc Construtor") 
        
obj=abc()

Parameterized constructor example:

class abc:
    x=100
    y=200
    def __init__(self, x, y): # takes arguments
        self.x = x   # Set number of cars
        self.y = y   # Set number of dolls
        print("I am the ToyBox constructor!")

obj=abc(10,20)


'''

# __init__ method is used to initialize the object's state

class abc:
    x=100
    y=200
    def __init__(self):
        print("Hello I am abc Construtor")
    
obj=abc()
obj.__init__()

'''
Output:
Hello I am abc Construtor

'''

# Memory address of the constructor

class Student:
    name = 'karan'
    def __init__(self):
        print(self)
        print('adding new students in database')
        
s1 = Student()
print(s1)

'''
Output:
<__main__.Student object at 0x100a25d30>
adding new students in database
<__main__.Student object at 0x100a25d30>

Explanation:
s1 and self are pointing to the same memory address


'''

# Edge case where return is used in a constructor

class abc:
    x=100
    y=200
    def __init__(self):
        return None

obj=abc()
print(obj)

'''
Output: (returns the memory address of the object, which changes every time)
something like this -> <__main__.abc object at 0x000001B5DDEA0A90>

'''

# obj attribute > class attribute (example)

class Student:
    college = "ABC"
    name = 'anonymous' # class attribute
    
    def __init__(self,name,marks):
        self.name = name # obj attribute > class attribute
        self.marks = marks
        print('adding new students in database')
s1 = Student('karan',97)
print(s1.name)


'''
Output:
adding new students in database
karan

Explanation:
if same 'name', object attribute will be given higher priority (not common practice)

'''

'''
Methods:

Functions that belong to objects
(always take self as an argument)
'''

# Example:

class Student:
    college = "ABC"
    
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks
    
    def welcome(self): # method
        print("Welcome", self.name, "to", self.college)
        
    def get_marks(self):
        return self.marks
        
s1 = Student('karan',97)
s1.welcome() # calling method 'welcome'
print(s1.get_marks()) # calling method 'get_marks' and printing the return value

'''
Output:
Welcome karan to ABC
97

'''

'''
Static Method:
Methods that dont use the self parameter (work at class level)

Decorators: Allow us to wrap another function 
in order to extend the behaviour of the wrapped function without permanently modifying it.

'''

# Example:

class Student:
    @staticmethod # decorator
    def college():
        print('ABC College')
        
Student.college()

# Get average mark of the students

class Student:
    
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks
    
    def average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(f"Hi {self.name}, your average mark is {sum/3}")
        
s1 = Student("tony",[99,98,87])
s1.average()

'''
Output:
Hi tony, your average mark is 94.66666666666667

'''

# Example of constructor used to print the value of the variables of the class

class abc:
    x=100
    y=200
    def __init__(self):
        print("Hello I am abc Construtor")
        
obj=abc()

obj.x=500 # overwrite the value of x
obj.y=1000
print(obj.x) 
print(obj.y)

# A case where we dont overwrite the value and print the value separately

class abc:
    x=100
    y=200
    def __init__(self):
        print("Hello I am abc Construtor")
    
    def fun(self):
        print(self.x)
        print(self.y)
    
    
    
obj=abc()
obj.x=1000
obj.y=2000

obj.fun() # calling the function prints the overwritten values of x and y


obj2=abc() 
obj2.fun() # calling the function prints the assigned values of x and y

'''

Output:
Hello I am abc Construtor
1000
2000
Hello I am abc Construtor
100
200


'''
# Printing using constructor through input

class abc:
    def __init__(self):
        self.x=input("Enter The value of the x ")
        self.y=input("Enter the value of y ")
        
    def display(self):
        print(self.x)
        print(self.y)
        
        
obj=abc()
obj.display()

'''
Output:

Enter The value of the x 10
Enter the value of y 20
10
20


'''

'''if we overwrite'''

class abc:
    def __init__(self,a,b):
        self.x=a
        self.y=b
        
    def display(self):
        print(self.x)
        print(self.y)
        
        
obj=abc(2000,3500)

obj.display()

'''
Output:
2000
3500

'''


# Example - Toybox

class ToyBox:
    def __init__(self, x, y):
        self.x = x   # Set number of cars
        self.y = y   # Set number of dolls
        print("I am the ToyBox constructor!")

    def show_toys(self):
        print("Cars:", self.x)
        print("Dolls:", self.y)

'''
__init__(self, x, y) means we expect x and y when creating a new object.
self.x = x stores that input inside the object.
Now, each object has its own toys, based on the inputs.
'''

box1 = ToyBox(50, 100)   # box1 has 50 cars, 100 dolls
box1.show_toys()

box2 = ToyBox(5, 10)     # box2 has 5 cars, 10 dolls
box2.show_toys()    # This prints: Cars: 5, Dolls: 10


'''
Output:

I am the ToyBox constructor!
Cars: 50
Dolls: 100
I am the ToyBox constructor!
Cars: 5
Dolls: 10


'''

