'''

Dunder methods - starts and ends with double underscore 
(used to do operation on objects)

Examples:

__init__
__str__
__len__

'''
# string
class ABC:
    x = "Lokesh"
    y = "DevCoder"
    
    def __init__(self):
        print("Hello i am ABC constructor")
        
    def __str__(self): # dunder method for string operations
        return self.x+self.y
    
    def __len__(self): # dunder method for return length for any datatype
        return len(self.x+self.y)
    
obj = ABC()
print(obj) # will print the value of x and y

# length
class ABC:
    x = "Lokesh"
    y = "DevCoder"
    
    def __init__(self):
        print("Hello i am ABC constructor")
    
    def __len__(self): # dunder method for return length for any datatype
        return len(self.x+self.y)
    
obj = ABC()
print(len(obj)) # will return the length of x and y

# Other dunder methods

class ABC:
    x = 100
    y = 200
    
    def __init__(self):
        print("Hello i am ABC constructor")
    
    def __add__(self,other): # dunder method for addition
        print(self.x+other.x)
    
    def __eq__(self,other): # dunder method for equality
        print(self.x == other.x)
    
    def __ne__(self,other): # dunder method for not equal to
        print(self.x != other.x)
    
    def __gt__(self,other): # dunder method for greater than
        print(self.x > other.x)
    
    def __ge__(self,other): # dunder method for greater than or equal to
        print(self.x >= other.x)
    
    def __lt__(self,other): # dunder method for less than
        print(self.x < other.x)
    
    def __le__(self,other): # dunder method for less than or equal to
        print(self.x <= other.x)
        
obj = ABC()
obj2 = ABC()

obj2.x = 900

obj <= obj2
