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



