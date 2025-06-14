# List as a iterator

arr = [10,20,30,40,50]

idx = iter(arr)

print(next(idx)) # prints 10
print(next(idx)) # prints 10, 20
print(next(idx)) # prints 10, 20, 30
print(next(idx)) # prints 10, 20, 30, 40
print(next(idx)) # prints 10, 20, 30, 40, 50

for i in range(5):
    print(next(idx)) # prints 10, 20, 30, 40, 50

'''
This prints depending on the number of times next(idx) is called.
It will throw an error if next(idx) is called more than the number of elements in the array

'''

# String as a iterator

mystr = 'Lokesh is the good boy'

for i in range(len(mystr)):
    print(next(idx)) # prints each character in the string


'''

Difference between iterator and generator is that,
iterator takes up memory and generator does not

Iterator is used for linear data types, so it uses memory.
Generator does't need linear data types to work. 
It works same as iterator but it does not take up memory and generates data in runtime.

return - break
yield - suspend (until i call the function again)

'''
# Generator

def myfunction(n):
    for i in range(n):
        yield i 
        
idx = myfunction(5) # generator (memory-efficient)

print(next(idx)) # prints 0 
print(next(idx)) # prints 0,1 
print(next(idx)) # prints 0,1,2
print(next(idx)) # prints 0,1,2,3
print(next(idx)) # prints 0,1,2,3,4
print(next(idx)) # prints 0,1,2,3,4

for i in idx:
    print(i) # prints 0,1,2,3,4


# Function as a iterator

def myfunction(n):
    for i in range(10,n,2):
        yield i

idx = myfunction(20)

print(next(idx)) # prints 10
print(next(idx)) # prints 10, 12
print(next(idx)) # prints 10, 12, 14


