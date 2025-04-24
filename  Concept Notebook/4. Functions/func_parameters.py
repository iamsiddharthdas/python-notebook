
'''
Actual and Formal Parameters in Python
1. Actual Parameters: These are the values that are passed to the function when it is called. They are also known as arguments.
2. Formal Parameters: These are the variables that are defined in the function definition. They act as placeholders for the actual parameters.
3. When a function is called, the actual parameters are passed to the formal parameters in the order they are defined.
4. The number of actual parameters must match the number of formal parameters in the function definition.
5. If the number of actual parameters is less than the number of formal parameters, a TypeError will be raised.

'''

def fun(a,b,c,d,e): # Formal parameters
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    
fun(10,20,66.77, "Hum Honge Kaamyaab", False) # Actual parameters

'''
Output:
10
20
66.77
Hum Honge Kaamyaab
False

Explanation:
1. The function fun() is defined with five formal parameters: a, b, c, d, and e.
2. The function is called with five actual parameters: 10, 20, 66.77, "Hum Honge Kaamyaab", and False.
3. The values of the actual parameters are passed to the corresponding formal parameters in the function.
4. The function prints the values of the formal parameters.
5. The output shows the values of the actual parameters in the order they were passed to the function.

'''

def fun1(a,b,c): # Formal parameters
    print(a)
    print(b)
    print(c)
    
fun1(10,20,66.77, "Hum Honge Kaamyaab") # Actual parameters

'''
Output: TypeError
fun1() takes 3 positional arguments but 4 were given
Explanation:
1. The function fun1() is defined with three formal parameters: a, b, and c.
2. The function is called with four actual parameters: 10, 20, 66.77, and "Hum Honge Kaamyaab".
3. Since the number of actual parameters (4) does not match the number of formal parameters (3), a TypeError is raised.
4. The error message indicates that the function fun1() takes 3 positional arguments but 4 were given.
5. To fix this error, either reduce the number of actual parameters to 3 or increase the number of formal parameters in the function definition.
6. The output shows the error message indicating the mismatch in the number of arguments.
7. The function fun1() is not executed because of the error.
8. The error message is displayed instead of the expected output.


'''