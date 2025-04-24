'''
For Loop types in Python

1. For loop with range
2. For loop with in 
3. For loop with zip
4. For loop with enumerate

'''

'''
For loop with range
Three parameters:
1. Initialisation
2. Condition
3. Increment/Decrement
'''

# Example:
for i in range(0,5,1):
    print(i)
# prints 0, 1, 2, 3, 4

# '0' represents initialisation
# '5' represents condition
# '1' represents increment (positive means increment, negative means decrement)

'''
If Initialisation > Condition, greater than or equal to, then decrement
If Initialisation < Condition, less than or equal to, then increment
'''

# Example:
for i in range(5,0,-1):
    print(i)        
# prints 5, 4, 3, 2, 1

for i in range(0,5,1):  
    print(i)
# prints 0, 1, 2, 3, 4


'''
Using break, continue and exit() in for loop
1. Break: Used to exit the loop
2. Continue: Used to skip the current iteration and continue with the next iteration
3. Exit: Used to exit the program

'''

# break()
# Example: 
for i in range(0,5,1):
    if i == 3:
        break
    print(i)
print('Hello World')

'''
Output: 
0
1
2
Hello World

̉'''

for i in range(0,5,1):
    break
    print(i)
print('Hello World')

'''
Output:
Hello World
'''

# exit()
# Example:

for i in range(0,5,1):
    if i == 3:
        exit()
    print(i)
    
print('Hello World')

'''
Output:
0
1
2

'''

# continue()
# Example:
for i in range(0,5,1):
    if i == 3:
        continue
    print(i)
'''
Output:
0
1
2
4

'''

for i in range(0,10,1):
    if i == 4 or i == 8:
        continue
    print(i)
print('Hello World')

'''
Output:
0
1
2
3
5
6
7
9
Hello World

'''

