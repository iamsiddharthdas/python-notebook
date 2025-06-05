
'''
difference between error and exception

Exception can be handled but error cannot be handled.

'''
try:
    print(5/0)
    
except Exception as e:
    print(e)
    
finally:
    print("It will print anyway")
    

'''
Output:
ZeroDivisionError: division by zero
It will print anyway
'''