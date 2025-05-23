'''

Set is a collection of unique elements.
It is mutable
Set is similar to dictionary but it is does not allow duplicate values.

x = {1, 2, 3, 4, 5}
print(type(x)) # prints <class 'set'>

x = {1, 2, 3, 4, 4}
print(type(x)) # prints <class 'set'> 
# Set will remove the duplicate values

Set is unordered. So index dont work.

'''

# Typecasting to list and set 

x = [10,20,20,30,30,30]
x = set(x)
x = list(x)
print(x) # prints [10, 20, 30] -> Set will remove the duplicate values

# add and discard

x = {10,20,30}
x.add(40)
print(x) # prints {10, 20, 30, 40}
x.discard(30)
print(x) # prints {10, 20, 40}

# union, intersection, difference and symmetric_difference

x = {10,20,30}
y = {30,40,50}
print(x.union(y)) # prints {10, 20, 30, 40, 50} -> It will put all the unique values in a set
# print(x | y) -> Union

print(x.intersection(y)) # prints {30} # It will put all the common values in a set
# print(x & y) -> Intersection

print(x.difference(y)) # prints {10, 20} # It will put all the values in x that are not in y
# print(x - y) -> Difference

print(x.symmetric_difference(y)) # prints {10, 20, 40, 50} # It will put all the unique values in x and y
# print(x ^ y) -> Symmetric Difference


# set is only iterable in for-in loop
for i in x:
    print(i) # prints 10,20,30

# clear

x = {10,20,30}
x.clear()
print(x) # prints set()

# copy

x = {10,20,30}
y = x.copy()
print(y) # prints {10, 20, 30}