
'''
LEGB
Local, Enclosing, Global, Built-in
'''
# Local scope: The innermost scope, which is the local scope of the function. e.g. 

def test():
    x = 'local x'
    print(x)
test()

'''
prints -> local x because x is defined in the local scope of the function test().

'''

# Enclosing scope: The scope of the enclosing function, if any. e.g.



def outer():
    x = 'enclosing x'
    def inner():
        print(x)
    inner()
outer()
'''
prints -> enclosing x because x is defined in the enclosing scope of the function outer().

'''

# Global scope: The outermost scope, which is the global scope. e.g.

x = 'global x'
def test():
    print(x)
test()

'''
prints -> global x because x is defined in the global scope.

'''

# Built-in scope: The outermost scope, which is the built-in scope. e.g.


import builtins
print(builtins.len('Test'))

'''
prints -> 4 because len() is a built-in function that returns the length of the string 'Test'.

'''

# How LEGB works in Python:



# example:

x = 'global x'

def test():
    y = 'local y'
    print(y)
    
test()

''' 
prints -> local y because y is defined in the local scope of the function test() and comes first in the LEGB order.

'''

# example:
x = 'global x'
def test():
    y = 'local y'
    print(x)

test()

''' 
prints -> global x 

Following the LEGB order:
First, its looks for global x in local scope, but it doesn't find it. 
Then it looks for x in the enclosing scope, but it doesn't find it. 
Then it looks for x in the global scope and finds it. So, it prints global x.

'''

# example:
x = 'global x'

def test():
    y = 'local y'
    print(x)
test()
print(y)

'''
prints -> 
NameError: name 'y' is not defined because 
y is defined in the local scope of the function test() and is not accessible outside the function.

'''
# example:
x = 'global x'
def test():
    x = 'local x'
    print(x)
test()
print(x)

'''
prints ->
local x
global x


Following the LEGB order:
First, it looks for x in the local scope of the function test() and finds it.
Then it prints local x.
After that, it looks for x in the enclosing scope, but it doesn't find it.
Then it looks for x in the global scope and finds it. So, it prints global x.

Why Global variable didn't overwrite local variable?
Because the local variable x is defined in the local scope of the function test() and is not accessible outside the function. 
'''

#How to access global variable inside a function?
#To do this, we can explicitly tell python that the x variable we want to use is the global x variable.

# example:
x = 'global x'
def test():
    global x # we use the 'global' keyword to tell python that we want to use the global x variable
    x = 'local x'
    print(x)
test()
print(x)

'''
prints ->
local x
local x

Explanation:
Now local x looks a bit missleading because it is actually the global x variable that we are modifying.
It's no longer in the local scope, it is now in the global scope.

'''

# What if we comment out the line global x?


# x = 'global x'

def test():
    global x
    x = 'local x'
    print(x)
    
test()
print(x)

''' 
prints -> 
local x
local x

Explanation: The outer print(x) still finds the global x as it is defined in the function test().
'''

# So what happens if we comment out the line global x inside the function test()?

# x = 'global x'
def test():
    # global x
    x = 'local x'
    print(x)
test()
print(x)

'''
local x
NameError: name 'x' is not defined

Explanation:
1. The first print(x) inside the function test() prints local x because it is defined in the local scope of the function.
2. The second print(x) outside the function raises a NameError because x is not defined in the global scope.

'''

def test(z):
    x = 'local x'
    print(x)
    print(z)
test('local z')

'''
prints ->
local z

Explanation:
1. First it looks for z in the local scope of the function test() and finds it.
2. Then it prints local z because it is defined in the local scope of the function test() and is passed as an argument to the function.


'''
def test(z):
    x = 'local x'
    print(z)
test('local z')
print(z)

'''
prints ->
local z
NameError: name 'z' is not defined

Explanation:
1. The first print(z) inside the function test() prints local z because it is defined in the local scope of the function.
2. The second print(z) outside the function raises a NameError because z is not defined in the global scope.

'''

# How Buitin scope works:

# example:
import builtins

def min():
    pass

m = min ([1, 2, 3, 4, 5])
print(m)

'''

Explanation:

Python found min() in the global scope before it found in the builtin scope.

'''

import builtins

def my_min(): # changed the function name to avoid conflict with built-in min
    pass

m = min ([1, 2, 3, 4, 5])
print(m)

'''
Explanation: Now it doesn't find 'min' in the global scope, and uses the built-in 'min' function as expected.

'''
# Function inside a function:

def outer():
    x = 'outer x'
    def inner():
        x = 'inner x'
        print(x)
    inner()
    print(x)
    
outer()

'''
prints ->
inner x
outer x

Explanation: (following the LEGB order)

1. First it looks for x in the local scope of the function inner() and finds it.
2. Then it prints inner x because it is defined in the local scope of the function inner().
3. Then it looks for any local x variable in the local scope of the function outer(), and finds it.
4. Then it prints outer x because it is defined in the local scope of the function outer().

'''

def outer():
    x = 'outer x'
    def inner():
        # x = 'inner x'
        print(x)
    inner()
    print(x)
    
outer()

'''
prints ->
outer x
outer x

This is what is called Enclosing Scope.

Explanation: (Following the LEGB order)

1. First print(x) [defined in inner()] looks for x in the local scope of the function inner() and doesn't find it.
2. Then it looks for x in the local scope of any enclosing function (enclosing scope) i.e outer() and finds it. Prints outer x.
3. Second print(x) [defined in outer()] looks for x in the local scope of the function outer() and finds it. Prints outer x.

'''
# Now if we comment out outer x in outer() instead of inner x in inner():

def outer():
    # x = 'outer x'
    def inner():
        x = 'inner x'
        print(x)
    inner()
    print(x)
    
outer()

'''
Prints
inner x
NameError: name 'x' is not defined

Explanation: (following the LEGB order)
1. The first print(x) inside the function inner() prints inner x because it is defined in the local scope of the function inner().
2. The second print(x), which is outside of inner(), doesn't find any local x variable in outer() function.
3. Then it looks for x in the enclosing scope, but it doesn't find it.
4. Then it looks for x in the global scope and doesn't find it.
5. Then it looks for x in the built-in scope and doesn't find it.
6. Hence, it raises a NameError because x is not defined in any scope.


'''

# Using Nonlocal x in inner():

def outer():
    x = 'outer x'
    def inner():
        nonlocal x
        x = 'inner x'
        print(x)
    inner()
    print(x)
    
outer()

'''
Nonlocal x means it can modify the x variable both in local and enclosing scope, but not in global/built-in scope.

prints ->
inner x
inner x

Explanation: (Following the LEGB order)

1. First print(x) [defined in inner()] looks for x in the local scope of the function inner() and finds it. Prints inner x.
2. Then it looks at nonlocal x in the local scope of the function inner(). So it modifies the local and enclosing x variable in outer() function as well.
3. Second print(x) [defined in outer()] prints inner x as it the value of x in the outer() is now modified to inner x.


It is better to use Nonlocal instead of Global because it doesn't pollute the global scope.

'''

x = 'global x'
def outer():
    x = 'outer x'
    def inner():
        x = 'inner x'
        print(x)
    inner()
    print(x)
    
outer()
print(x)

'''
prints -> (following the LEGB order)
inner x
outer x
global x

'''
# for a in range(2):
#     x = 'global {}'.format(a)


# def outer():
#     # x = 'outer x'
#     for b in range(3):
#         x = 'outer {}'.format(b)

#     def inner():
#         # x = 'inner x'
#         for c in range(4):
#             x = 'inner {}'.format(c)
#         print(x)
#         print(a, b, c)

#     inner()
#     print(x)
#     print(a, b)

# outer()
# print(x)
# print(a)

