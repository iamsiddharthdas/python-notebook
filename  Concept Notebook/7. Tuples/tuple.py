'''

Tuple is used to store static data.
It is immutable, meaning it cannot be changed after creation. 
Tuple is ordered, meaning the items have a defined order, and that order will not change.
'''



tuple = (10,20,30,40,50)

print(tuple) # prints (10, 20, 30, 40, 50)
print(tuple[0]) # prints 10
print(tuple[1]) # prints 20
print(tuple[2]) # prints 30
print(tuple[3]) # prints 40
print(tuple[4]) # prints 50

'''
Tuples and Lists are objects - - it uses heap memory (just like list)


In-built functions that can be used in tuples are:
count()
index()

'''
# index() - returns the index of the first occurrence of the specified value

tuple = (10,20,30,40,50)
print(tuple.index(30)) # prints 2

# count() - returns the number of times the specified value appears in the tuple

tuple = (10,20,30,40,50)
print(tuple.count(30)) # prints 1


'''
How to modify a tuple?
We can convert a tuple to a list, modify the list, and then convert the list back to a tuple.

Typecasting functions that can be used

int()
float()
str()
bool()
list()
tuple()
set()
dict()


'''

x = (10,20,30,40,50)

x = list(x) # converts the tuple to a list

x.append(200) # prints [10, 20, 30, 40, 50, 200]

x = tuple(x) # converts the list to a tuple

print(tuple) # prints (10, 20, 30, 40, 50, 100)


# 2d array with tuples

x = [(10,20,30),(40,50,60),(70,80,90)]

for i,j,k in x:
    print(i,j,k)
    
'''
Output:

(10, 20, 30)
(40, 50, 60)
(70, 80, 90)


'''