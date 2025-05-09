# Linear search

x = [10,20,30,40,60,32,21]

value = int(input("Enter the value "))

for i in range(len(x)): # iterate through the list
    if x[i] == value: # check if the element is present
        print("Element found") 
        exit() 

print("Element not found")

'''
Not a good approach because for loop will run for all the elements in the list
So for large lists, it will take a lot of time
Better approach is to use binary search.

'''
# Binary search

'''
For binary search, the list should be sorted
Lower bound - the first index of the list
Mid bound - the middle index of the list -> Low + High // 2
High bound - the last index of the list

Right search - Lower = mid + 1
Left search - High = mid - 1

'''

def Binary_Search(arr,sval):
    arr.sort() # sort the list
    
    lower = 0 # lower bound
    high = len(arr) - 1 # high bound
    
    while lower <= high: # while lower is less than or equal to high
        mid = (lower + high) // 2
        if arr[mid] == sval:
            return True
        elif arr[mid] < sval:
            lower = mid + 1
        else:
            high = mid - 1
    
    return False

flag = Binary_Search(x,40) 

if flag == True:
    print("Element found")
else:
    print("Element not found")
    
    