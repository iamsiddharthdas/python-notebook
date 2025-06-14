'''
List inside a list (2D array)

'''

x = [[10,20,30],[40,50,60],[70,80,90]]


'''
print (x[0]) # prints the first list i.e. [10,20,30]
print (x[1]) # prints the second list i.e. [40,50,60]
print (x[2]) # prints the third list i.e. [70,80,90]


print (x[0][0]) # prints the first element of the first list i.e. 10
print (x[0][1]) # prints the second element of the first list i.e. 20
print (x[0][2]) # prints the third element of the first list i.e. 30
print (x[1][0]) # prints the first element of the second list i.e. 40
print (x[1][1]) # prints the second element of the second list i.e. 50
print (x[1][2]) # prints the third element of the second list i.e. 60
print (x[2][0]) # prints the first element of the third list i.e. 70
print (x[2][1]) # prints the second element of the third list i.e. 80
print (x[2][2]) # prints the third element of the third list i.e. 90

'''         

# Printing a 2D array by taking input from user

x = []

for i in range(3):
    x.append([])
    for j in range(3):
        temp = int(input("Enter the element: "))
        x[i].append(temp)
        
print("The 2D array is: ",x)

'''
Output:
Enter the element: 10
Enter the element: 20
Enter the element: 30
Enter the element: 40
Enter the element: 50
Enter the element: 60
Enter the element: 70
Enter the element: 80
Enter the element: 90

The 2D array is:  [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

'''

# Printing all the elements of the 2D array using nested for loop

for i in range(len(x)): 
    for j in range(len(x[i])): 
            print (x[i][j]) 

'''
Output:
10
20
30
40
50
60
70
80
90

'''

'''
For Matrix formation of 2D array

Like this,

[10,20,30]
[40,50,60]
[70,80,90]

'''
x = [[10,20,30],[40,50,60],[70,80,90]]

for i in range(len(x)):
    for j in range(len(x[i])):
        print(x[i][j],end=" ")
    print(end="\n") # this will print the 2D array in matrix form
    

'''
Output:

10 20 30 
40 50 60 
70 80 90 

'''
# Printing all the elements of the 2D array using nested for loop (taking input from user)

x = []
n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
for i in range(n):
    row = []
    for j in range(m):
        row.append(int(input("Enter the element: ")))
    x.append(row)
print("The 2D array is: ")

for i in range(len(x)):
    for j in range(len(x[i])):
        print(x[i][j],end=" ")
    print(end="\n") # this will print the 2D array in matrix form

'''
Output:

Enter the number of rows: 3
Enter the number of columns: 3
Enter the element: 1
Enter the element: 2
Enter the element: 3
Enter the element: 4
Enter the element: 5
Enter the element: 6
Enter the element: 7
Enter the element: 8
Enter the element: 9

The 2D array is:
1 2 3
4 5 6
7 8 9

'''


# Addition and subtraction of two 2D arrays (matrix addition and subtraction)

x = [[10,20,30],[40,50,60],[70,80,90]]

y = [[100,110,130],[210,220,230],[310,320,330]]

z =[]

for i in range(3):
    z.append([])
    for j in range(3):
        z[i].append(x[i][j] + y[i][j]) # this will add the two 2D arrays
        # z[i].append(x[i][j] - y[i][j]) # this will subtract the two 2D arrays

print(z) # this will print the sum of the two 2D arrays


# Multiplication of two 2D arrays (matrix multiplication)

x = [[10,20,30],[40,50,60],[70,80,90]]

y = [[1,1,1],[2,2,2],[3,3,3]]

z = []

for i in range(len(x)):
    z.append([]) 
    for j in range(len(x[i])): 
        z[i].append(0) # this will create a new list for each column of the 2D array
        for k in range(len(y)):
            z[i][j] += x[i][k] * y[k][j] # this will multiply the two 2D arrays
            # z[i][j] += x[i][k] / y[k][j] # this will divide the two 2D arrays

print(z) # this will print the product of the two 2D arrays


# Transformation of 2D array (matrix transformation)

'''
Row becomes column and column becomes row
Like this,

[10,20,30]     [10,40,70]
[40,50,60]  => [20,50,80]
[70,80,90]     [30,60,90]

'''

x = [[10,20,30],[40,50,60],[70,80,90]]

for i in range(len(x)):
    for j in range(len(x[i])):
        print(x[j][i],end=" ") # row becomes column and column becomes row
        
    print(end="\n") # this will print the 2D array in matrix form

# Removing duplicates from a 2D array

'''
You can remove duplicates from a 2D array by using a set to store the unique elements and then converting the set back to a list.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3],
    [7, 8, 9]
]

unique_matrix = []
for row in matrix:
    if row not in unique_matrix:
        unique_matrix.append(row)

print("Matrix without duplicate rows:")
for row in unique_matrix:
    print(row)

'''

x = [10,20,20,30,20,10,80,81,60,42,2,31,2,1,1,1]

y = []

for i in range(len(x)):
    if x[i] not in y:
        y.append(x[i]) # this will add the x array to the y array if it is not already present in the y array

print("The array without duplicates is: ",y) # this will print the array without duplicates

'''
Output:
The array without duplicates is:  [10, 20, 30, 80, 81, 60, 42, 2, 31, 1]

'''

# List comprehension

'''

Why do we use list comprehension?

You can declare and filter elements in a list using loops (for, if, else) 
and conditions in a single line using list comprehension.

How to use list comprehension?

If you are using for loop with only 'if' condition, you have to write on the right of the 'for' loop.
But if you are using 'if' and 'else' condition, you have to write on the left of the 'for' loop.

'''
# Declaring elements in the array using list comprehension
x = [i for i in range(10)]

print(x)

'''
Output:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

'''

x = [i for i in range(10) if i % 2 == 0]

print(x)

'''
Output:
[0, 2, 4, 6, 8]

'''

# Filtering elements in the array using list comprehension
y = [11,10,20,22,31,45,67,83,75]

x = [y[i] for i in range(len(y)) if y[i] % 2 != 0]
# this will add the y array to the x array if it is odd

print(x)


y = [11,10,20,22,31,45,67,83,75]

x = [y[i] for i in range(len(y)) if y[i] % 2 != 0]
# this will add the y array to the x array if it is odd

print(x)

'''
Output:
[11, 31, 45, 67, 83, 75]

'''
# Odd and Even numbers in the array using list comprehension

y = [11,10,20,22,31,45,67,83,75]

x =[y[i] if y[i]%2==0 else True for i in range(len(y))] 
# prints True if the value is odd
# prints the element if the value is even

print(x)

'''
Output:
[True, 10, 20, 22, True, True, True, True, True]

'''

y = [11,10,20,22,31,45,67,83,75]
x =[y[i] if y[i]%2==0 else 'Odd Value' for i in range(len(y))] 
# prints 'Odd Value' if the value is odd
# prints the element if the value is even

print(x)

'''
Removing duplicates from a list using list comprehension

'''

x = [10,10,11,20,40,50,30,11,40,66,98,90,44,34,33,22]
y = []
z = [y.append(i) for i in x if i not in y] 
# this will add the elements of x to y if they are not already present in y

print("The array without duplicates is: ",y) 
# this will print the array without duplicates

'''
Output:
The array without duplicates is:  [10, 11, 20, 40, 50, 30, 66, 98, 90, 44, 34, 33, 22]

'''


'''
List inside a List inside a List (3D array)

'''

x = [[[10,20,30],[40,50,60],[70,80,90]],[[100,200,300],[400,500,600],[700,800,900]]]


'''
print (x[0]) # prints the first list i.e. [[10,20,30],[40,50,60],[70,80,90]]
print (x[1]) # prints the second list i.e. [[100,200,300],[400,500,600],[700,800,900]]

print (x[0][0]) # prints the first element of the first list i.e. [10,20,30]
print (x[0][1]) # prints the second element of the first list i.e. [40,50,60]
print (x[0][2]) # prints the third element of the first list i.e. [70,80,90]
print (x[1][0]) # prints the first element of the second list i.e. [100,200,300]
print (x[1][1]) # prints the second element of the second list i.e. [400,500,600]
print (x[1][2]) # prints the third element of the second list i.e. [700,800,900]

print (x[0][0][0]) # prints the first element of the first list i.e. 10
print (x[0][0][1]) # prints the second element of the first list i.e. 20
print (x[0][0][2]) # prints the third element of the first list i.e. 30
print (x[0][1][0]) # prints the first element of the second list i.e. 40
print (x[0][1][1]) # prints the second element of the second list i.e. 50
print (x[0][1][2]) # prints the third element of the second list i.e. 60
print (x[0][2][0]) # prints the first element of the third list i.e. 70
print (x[0][2][1]) # prints the second element of the third list i.e. 80
print (x[0][2][2]) # prints the third element of the third list i.e. 90
print (x[1][0][0]) # prints the first element of the first list i.e. 100
print (x[1][0][1]) # prints the second element of the first list i.e. 200
print (x[1][0][2]) # prints the third element of the first list i.e. 300
print (x[1][1][0]) # prints the first element of the second list i.e. 400
print (x[1][1][1]) # prints the second element of the second list i.e. 500
print (x[1][1][2]) # prints the third element of the second list i.e. 600
print (x[1][2][0]) # prints the first element of the third list i.e. 700
print (x[1][2][1]) # prints the second element of the third list i.e. 800
print (x[1][2][2]) # prints the third element of the third list i.e. 900

'''

# Printing all the elements of the 3D array using nested for loop

for i in range(len(x)): 
    for j in range(len(x[i])): 
        for k in range(len(x[i][j])): 
            print (x[i][j][k])

'''
Output:
10
20
30
40
50
60
70
80
90
100
200
300
400
500
600
700
800
900

'''



