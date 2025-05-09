
'''
Functions are of two types:
User defined functions - functions that are defined by the user
Library functions - functions that are defined by the library

Library functions are built-in functions that are provided by the Python library.
It is used to perform specific tasks and is available in the Python library.

'''

# Simple example of library functions


import math

square_root = math.sqrt(81)
# square root of 81 

print(square_root) # print 9

exponent = pow(2,3)

#pow() executes the exponent of number. here its 2^3 

print(exponent) # prints 8



'''
append() - adds to the last of the list
insert() - adds to the specific index of the list
pop() - removes the last element of the list(if no index is given)

'''

# Append() example

x = [1,2,3,4,5]
x.append(6) # appends 6 to the last of the list
print(x) # prints [1,2,3,4,5,6]

# insert() example

y = [1,2,3,4,5]
y.insert(2, 10) # inserts 10 to the index 2 of the list
print(y) # prints [1,2,10,3,4,5]

# pop() example

z = [1,2,3,4,5]
z.pop() # removes the last element of the list
print(z) # prints [1,2,3,4]

z.pop(2) # removes the element at index 2 of the list
print(z) # prints [1,2,4]

'''
del keyword - deletes anything. variable, element in the list, etc.
'''

list1 = [1,2,3,4,5]
del list1[2] # deletes the element at index 2 of the list
del list1 # deletes the list

'''
sort() - sorts the list in ascending order
x.sort(reverse=True) - sorts the list in descending order
reverse() - reverses the list (not descending order)
clear() - clears the list
'''

list2 = [5,4,2,10,1]

list2.sort() # sorts the list in ascending order
print(list2) # prints [1,2,4,5,10]

list2.sort(reverse=True) # sorts the list in descending order
print(list2) # prints [10,5,4,2,1]

list2.reverse() # reverses the list
print(list2) # prints [1,2,4,5,10]

list2.clear() # clears the list
print(list2) # prints [] - empty list

# Without using insert() function

x = [10, 20, 30, 40, 60, 32, 21]
y = [] # create a new list
for i in range(len(x)): # iterate through the list
    if i == 4: 
        y.append(50)
    y.append(x[i]) # append the element to the new list
x = y # assign the new list to the old list
print(x)

# Adding to the list through index and value input

x=[10,20,30,40,60,32,21]

temp=int(input("Enter the Value of Temp "))
x.append(temp)
postion=int(input("Enter the Position "))
for i in range(len(x)-1,postion,-1):
    t=x[i]
    x[i]=x[i-1]
    x[i-1]=t
    
print(x)

# DSA style (no library functions)

# Original list
x = [10, 20, 30, 40, 60, 32, 21]

# Take input
index = int(input("Enter the index to insert at: "))
value = int(input("Enter the value to insert: "))

# Step 1: Move last element to a temp variable (buffer)
last = x[len(x) - 1]

# Step 2: Shift elements to the right to make space at the index
i = len(x) - 1
while i > index:
    x[i] = x[i - 1]
    i -= 1

# Step 3: Insert the new value
x[index] = value

# Step 4: Manually remove the last element (set it to dummy or ignore it)
# Here we’ll create a new list of length -1
y = []
for i in range(len(x) - 1):
    y = y + [x[i]]  # Avoid using append()

# Final output
print(y)

# Using only pop()

x = [10, 20, 30, 40, 60, 32, 21]

temp=int(input("Enter the Value of Temp "))
position  = int(input("Enter index: "))

for i in range(position,len(x)-1,1):
    temp = x[i]
    x[i] = x[i+1]
    x[i+1] = temp
    
x.pop()

print(x)


