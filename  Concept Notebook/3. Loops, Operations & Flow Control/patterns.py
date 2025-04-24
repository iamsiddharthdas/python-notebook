
# Square Pattern (using numbers)

for i in range (1,5):
    for j in range(1,5):
        print(j,end=' ')
    print(end='\n')

'''
Output:
1  2  3  4
1  2  3  4
1  2  3  4
1  2  3  4

'''
# Square Pattern (using '*')

for i in range (1,5):
    for j in range(1,5):
        print('*',end=' ')
    print(end='\n')

'''
Output:
*  *  *  *
*  *  *  *
*  *  *  *
*  *  *  *

'''


# Butterfly Pattern

for i in range(4):
    for j in range(i+1):
        print("*",end=" ")
    print("    "*(5-i-1),end="")
    for k in range(i+1):
        print("*",end=" ")
    print(end="\n")

for i in range(4,-1,-1):
    for j in range(i+1):
        print("*",end=" ")
    print("    "*(5-i-1),end="")
    
    for k in range(i+1):
        print("*",end=" ")
    print(end="\n")
    
'''
Output:

*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 

'''