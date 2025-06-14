

i=1
fact=1
num=int(input("Enter a number "))

while i<=num:
    fact = fact*i
    i+=1
    
print("Factorial is", fact)

'''
let num = 5

i = 1, fact = 1*1 = 1
i = 2, fact = 1*2 = 2
i = 3, fact = 2*3 = 6
i = 4, fact = 6*4 = 24
i = 5, fact = 24*5 = 120
i = 6 -> greater than num -> Exits the loop and prints 

Output:
Factorial is 120

'''