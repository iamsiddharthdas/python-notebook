'''
Constructor in OOPS:

Properties:
1. It is used to initialize the object's state and perform any necessary setup operations.
2. In Python, constructors are defined using the __init__ method.
3. return statement cannot be used in __init__ method, except None. 

'''
# __init__ method is used to initialize the object's state

class abc:
    x=100
    y=200
    def __init__(self):
        print("Hello I am abc Contrutor")
    
obj=abc()
obj.__init__()

'''
Output:
Hello I am abc Contrutor

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

