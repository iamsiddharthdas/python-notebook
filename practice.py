class A:
    _x = 100  # protected variable
    y = 200
    
    def __init__(self):
        print("Hello i am A class constructor")
    def fun(self):
        print(self._x) 
        print("Hello i am A class fun method")
        
class B(A):
    a = 1500
    b = 1600
    
    def __int__(self):
        print(super()._x)
        
obj = B()