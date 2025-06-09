'''

Operator Overloading - polymorphism

When the same operator is allowed to have different meaning according to the context.

e.g. for '+' operator, 
print(1+2) -> 3 (addition)
print('a'+'b') -> ab (concatenation)
print([1,2]+[3,4]) -> [1,2,3,4] (merge)

This is Implicit Overloading (predefined in Python for different data types)


Lets take example of complex numbers

a = 1i+2j
b = 3i+4j
print(a+b) # (4+6j) -> real part(i) and imaginary part(j) are added separately

'''

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def shownNumber(self):
        print(self.real, "i +", self.imaginary, "i")
        
    def __add__(self,num2): # dunder method
        newReal = self.real + num2.real
        newImaginary = self.imaginary + num2.imaginary
        return Complex(newReal, newImaginary)
        
num1 = Complex(1,2)
num2 = Complex(3,4)

num1.shownNumber() # 1i + 2i
num2.shownNumber() # 3i + 4i

num3 =  num1 + num2 # possible because of __add__ dunder function
num3.shownNumber() # 4i + 6i

