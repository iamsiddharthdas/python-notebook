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


