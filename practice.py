def fun(x):
    if x>0:
        fun(x-1)
        print(x)
        fun(x-2)
        
fun(5)

'''
+------------------+------------------------------+
|  Function Call   |   Execution / Print Output   |
+------------------+------------------------------+
| fun(5)           |                              |
| fun(4)           |                              |
| fun(3)           |                              |
| fun(2)           |                              |
| fun(1)           |                              |
| fun(0)           | (x <= 0, no output)          |
| print(1)         | prints 1                     |
| fun(-1)          | (x <= 0, no output)          |
| print(2)         | prints 2                     |
| fun(0)           | (x <= 0, no output)          |
| print(3)         | prints 3                     |
| fun(1)           |                              |
| fun(0)           | (x <= 0, no output)          |
| print(1)         | prints 1                     |
| fun(-1)          | (x <= 0, no output)          |
| print(4)         | prints 4                     |
| fun(2)           |                              |
| fun(1)           |                              |
| fun(0)           | (x <= 0, no output)          |
| print(1)         | prints 1                     |
| fun(-1)          | (x <= 0, no output)          |
| print(2)         | prints 2                     |
| fun(0)           | (x <= 0, no output)          |
| print(5)         | prints 5                     |
| fun(3)           |                              |
| fun(2)           |                              |
| fun(1)           |                              |
| fun(0)           | (x <= 0, no output)          |
| print(1)         | prints 1                     |
| fun(-1)          | (x <= 0, no output)          |
| print(2)         | prints 2                     |
| fun(0)           | (x <= 0, no output)          |
| print(3)         | prints 3                     |
| fun(1)           |                              |
| fun(0)           | (x <= 0, no output)          |
| print(1)         | prints 1                     |
| fun(-1)          | (x <= 0, no output)          |
+------------------+------------------------------+



'''