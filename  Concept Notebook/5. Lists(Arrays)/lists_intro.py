
'''
Lists (Arrays) in Python

Lists are used to store multiple items in a single variable.
Lists are one of the most used data types in Python. 
They are mutable, meaning they can be changed after creation. 
Lists are ordered, meaning the items have a defined order, and that order will not change.

'''


x = [100,200,'Lokesh',True,1.5] # list of different data types

print(x[0]) # prints 100
print(x[1]) # prints 200
print(x[2]) # prints Lokesh
print(x[3]) # prints True
print(x[4]) # prints 1.5

print(x[-1]) # prints 1.5
print(x[-2]) # prints True
print(x[-3]) # prints Lokesh
print(x[-4]) # prints 200
print(x[-5]) # prints 100

print[len(x)-1] # prints 1.5
print(-len(x)) # prints 100

'''
List Slicing:

It is a way to get a subset of the list.
It is done by using the colon (:) operator.
The syntax is:
list[start:stop:step]
start - the starting index of the slice
stop - the ending index of the slice
step - the step size of the slice
If step is not given, it is assumed to be 1.
If start and stop are not given, it is assumed to be the whole list.

'''

# Example:

x = [100,200,'Lokesh',True,1.5] # list of different data types

x[0:2] # prints [100, 200] (start from 0 to 2)
x[1:3] # prints [200, 'Lokesh'] (start from 1 to 3)
x[1:] # prints [200, 'Lokesh', True, 1.5] (start from 1 to end)
x[::2] # prints [100, 'Lokesh', 1.5] (start from 0 to end with step size of 2)
x[::-1] # prints [1.5, True, 'Lokesh', 200, 100] (start from end to start)
x[::-2] # prints [1.5, 'Lokesh', 100] (start from end to start with step size of 2)
x[5:0:-2] # prints [1.5, True, 'Lokesh', 200] (start from 5 to 0 with step size of -2)
x[1:5:2] # prints [200, True] (start from 1 to 5 with step size of 2)
x[1:5] # prints [200, 'Lokesh', True, 1.5] (start from 1 to 5)
x[1:5:1] # prints [200, 'Lokesh', True, 1.5] (start from 1 to 5 with step size of 1)
x[1:5:3] # prints [200, True] (start from 1 to 5 with step size of 3)
x[1:5:4] # prints [200] (start from 1 to 5 with step size of 4)
x[1:5:5] # prints [] (start from 1 to 5 with step size of 5)
x[1:5:6] # prints [] (start from 1 to 5 with step size of 6)

# Index Error

y = [1,2,3,4,5]
i = 0
print(y[i+2+2+2]) # index out of range

# Printing using for loop

x = [100,200,'Lokesh',True,1.5] # list of different data types

for i in range(len(x)): # iterate through the list
    print(x[i]) # prints each element of the list

'''
Output:
100
200
Lokesh
True
1.5

'''
# Printing the list using while loop

x = [100,200,'Lokesh',True,1.5] # list of different data types

i=0
while i < len(x): # iterate through the list
    print(x[i]) # prints each element of the list in reverse order
    i = i + 1

'''
Output:
100
200
Lokesh
True
1.5

'''

# Reversing the list using for loop

x = [100,200,'Lokesh',True,1.5] # list of different data types

for i in range(len(x)-1,-1,-1): # iterate through the list in reverse order
    print(x[i]) # prints each element of the list in reverse order

'''
Output:
1.5
True
Lokesh
200
100

'''

# Reversing the list using while loop

x = [100,200,'Lokesh',True,1.5] # list of different data types

i = len(x) - 1
while i >= 0: # iterate through the list in reverse order
    print(x[i]) # prints each element of the list in reverse order
    i = i - 1

'''
Output:
1.5
True
Lokesh
200
100

'''
'''

Python Memory Management:

1. Stack Memory: Used for function calls and local variables. (single value variables and functions)

Stack has shared memory.
If a single value is assigned to two variables, both variables will point to the same memory location.
for example:
x = 10
y = 10
print(id(x)) # prints the memory location of x
print(id(y)) # prints the memory location of y

print(x is y) # prints True

Output:
4351009248
4351009248

(x and y will point to the same memory location)


2. Heap Memory: Used for dynamic memory allocation and global variables. (multi-value variables)

Even if the value is the same, the memory location will be different.
for example:
a = [1,2,3]
b = [1,2,3]

print(id(a)) # prints memory location of a 
print(id(b)) # # prints memory location of a 

print(x is y) # prints False

Output:
4376786752
4376627328

(a and b will point to the different memory locations)

Why is it like this?
Stack memory is faster than heap memory.
When a function is called, a new stack frame is created for that function call. When the function returns, the stack frame is removed from the stack. This allows for efficient memory management and prevents memory leaks.
Recursion uses stack memory to keep track of function calls and local variables. Each time a function calls itself, a new stack frame is created. When the base case is reached, the stack frames are removed one by one until the original function call returns.

'''

# 2D Lists

x = [[10,20,30],[30,40,50],[50,60,70]]

for i,j,k in x:
    print(i,j,k)
    
'''
Output:
10 20 30
30 40 50
50 60 70

'''