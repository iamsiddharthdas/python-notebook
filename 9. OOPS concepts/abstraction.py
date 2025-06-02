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


