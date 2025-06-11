arr = [10,20,30,40,50]
idx = iter(arr)

print(next(idx)) # prints 10
print(next(idx)) # prints 10, 20
print(next(idx)) # prints 10, 20, 30
print(next(idx)) # prints 10, 20, 30, 40
print(next(idx)) # prints 10, 20, 30, 40, 50

'''
This prints depending on the number of times next(idx) is called.
It will throw an error if next(idx) is called more than the number of elements in the array

'''
arr = [10,20,30,40,50]
idx = iter(arr)

for i in range(5):
    print(next(idx))
    
'''

Difference between iterator and generator is that,
iterator takes up memory and generator does not

'''