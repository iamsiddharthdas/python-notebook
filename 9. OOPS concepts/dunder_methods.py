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

# add 
class ABC:
    x= 100
    y= 200
    
    def __init__(self):
        print("Hello i am ABC contructor")
    
    def __add__(self,other):
        print(self.x+other.x)
        
obj=ABC()

obj2 = ABC()
obj.x = 1500
obj2.x = 3000

print(obj+obj2)

