'''
In Python, a lambda function, also known as an anonymous function, is a small, unnamed
function defined using the lambda keyword. Lambda functions are often used when you need
a simple function for a short period or when you want to define a function inline without
explicitly naming it.


'''

lambda: print("Hello World")

'''
In Python, lambda functions are declared using the lambda keyword, followed by the
parameter list, a colon (:), and the expression that defines the function's behavior.

lambda argument(s): expression

Here, we have defined a lambda function and assigned it to the variable named greet.
To execute this lambda function, we need to call it. Here's how we can call the lambda
function

In the above example, we have defined a lambda function and assigned it to
the greet variable.
When we call the lambda function, the print() statement inside the lambda function is
executed.

'''

greet = lambda: print("Hello World")

greet()


'''
In Python, you can create lambda functions with one or more arguments. Lambda functions
are defined using the lambda keyword, followed by a parameter list, a colon (:), and the
expression that defines the function's behavior.
Here's how you can create a lambda function with an argument:

'''
#lambda that accepts a single argument
greet_user = lambda name: print("Hello", name)

#lambda call
greet_user("John")

# Output: Hello John


'''
In the above example, we have assigned a lambda function to the greet_user variable.
Here, name after the lambda keyword specifies that the lambda function accepts the
argument named name.

Notice the call of the lambda function,
greet_user("John")

Here, we have passed a string value 'John' to our lambda function.
Finally, the statement inside the lambda function is executed.

'''
