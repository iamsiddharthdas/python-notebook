'''
Rotation is a process of moving the elements of an array in a circular manner.
For example, if we have an array [1,2,3,4,5] and we rotate it by 2 positions to the right, 
the array will become [4,5,1,2,3].

Left rotation - last element will be moved to the first position
Right rotation - first element will be moved to the last position

'''

def left_rotate(arr):

    temp = arr.pop() # remove the last element
    
    arr.insert(0,temp) # insert the last element at the first position
    print('Left rotated array -> ',arr) # print the rotated array

x = [10,11,21,16,81,62,82]

left_rotate(x) # call the left_rotate function

def right_rotate(arr):
    temp = arr.pop(0) # remove the first element
    arr.append(temp) # insert the first element at the last position
    print('Right rotated array -> ',arr) # print the rotated array
    
x = [10,11,21,16,81,62,82]

right_rotate(x) # call the right_rotate function

# Rotate 2 or more elements

def left_rotate(arr, n):
    for i in range(n):
        temp = arr.pop() # remove the last element
        arr.insert(0,temp) # insert the last element at the first position
    print('Left rotated array -> ',arr) # print the rotated array
x = [10,11,21,16,81,62,82]
n = 2 # number of positions to rotate
left_rotate(x, n) # call the left_rotate function

def right_rotate(arr, n):
    for i in range(n):
        temp = arr.pop(0) # remove the first element
        arr.append(temp) # insert the first element at the last position
    print('Right rotated array -> ',arr) # print the rotated array
x = [10,11,21,16,81,62,82]
n = 2 # number of positions to rotate
right_rotate(x, n) # call the right_rotate function

'''
Merging two arrays can be done using extend() function

'''
x = [10,20,30,40,50]
y = [100,200,300,500]

x.extend(y) # this will merge the two arrays
print(x) # print the merged array

'''
Merging without using extend() function
This can be done using a for loop

'''
x = [10,20,30,40,50]
y = [100,200,300,500]

for i in range(len(y)):
    y.append(x[i]) # this will merge the two arrays

print(x) # print the merged array






