
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


##

try:
    
    raise Exception("Hello")

except Exception as e:
    print(e)   

##

try:
    
    x={
        'a':100,
        'b':200,
        'c':300,
    }
    
    print(x['d'])

except Exception as e:
    print("Exception:",e)
    
