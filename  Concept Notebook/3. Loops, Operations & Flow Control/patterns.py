
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

i is the row number
j is the column number

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

i is the row number
j is the column number

'''

# Right-angled Triangle Pattern

for i in range(5):
    for j in range(i+1):
        print('*', end =' ')
    print(end='\n')

'''
Output:
*
*  *
*  *  *
*  *  *  *
*  *  *  *  *

i is the row number 
j is the column number

'''

''' * = i '''

for i in range(5):
    for j in range(i+1):
        print(i, end =' ')
    print(end='\n')

'''
Output: (prints i)
0              i=0, j=0
1  1           i=1, j=0,1
2  2  2        i=2, j=0,1,2
3  3  3  3     i=3, j=0,1,2,3
4  4  4  4  4  i=4, j=0,1,2,3,4

i is the row number (prints) -> repeats
j is the column number (iterates) -> increments

'''


''' * = j '''

for i in range(5):
    for j in range(i+1):
        print(j, end =' ')
    print(end='\n')

'''

Output: (prints j)

0              i=0, j=0
0  1           i=1, j=0,1
0  1  2        i=2, j=0,1,2
0  1  2  3     i=3, j=0,1,2,3
0  1  2  3  4  i=4, j=0,1,2,3,4

i is the row number (iterates) -> increments
j is the column number (prints) -> repreats 


'''

'''
Using ASCII values
'''
for i in range(5):
    for j in range(i+1):
        temp = "A"
        temp = ord(temp) # ASCII converted to integer i.e 65
        temp = temp + j # ASCII is incremented by j i.e 65+1=66
        temp = chr(temp) # ASCII conversion to character i.e 66 = B
        print(temp, end =' ')
    print(end='\n')
    
'''
Output: (j is involved)

A           i=0, j=0
A B         i=1, j=0,1
A B C       i=2, j=0,1,2
A B C D     i=3, j=0,1,2,3
A B C D E   i=4, j=0,1,2,3,4


i is the row number (iterates) -> increments
j is the column number (prints) -> repreats

'''
for i in range(5):
    for j in range(i+1):
        temp = "A"
        temp = ord(temp) # ASCII converted to integer i.e 65
        temp = temp + i # ASCII is incremented by j i.e 65+1=66
        temp = chr(temp) # ASCII conversion to character i.e 66 = B
        print(temp, end =' ')
    print(end='\n')
    
'''
Output: (i is involved)

A          i=0, j=0
B B        i=1, j=0,1 
C C C      i=2, j=0,1,2
D D D D    i=3, j=0,1,2,3
E E E E E  i=4, j=0,1,2,3,4

i is the row number (prints) -> repeats
j is the column number (iterates) -> increments

'''

# Inverted Right-angled Triangle Pattern

for i in range(5,-1,-1):
    # print(' ' * (5-i), end='') -> this condition is for converting right-angled triangle to equilateral triangle
    for j in range(i+1):
        print('*', end=' ')
    print(end='\n')
    
'''
Output:

* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 

'''

for i in range(5,0,-1):
    for j in range(5,i,-1):
        print(j, end =' ')
    print(end='\n')

'''
Output: (prints j)

5  4  3  2  1   i=0, j=5,4,3,2,1
5  4  3  2      i=1, j=5,4,3,2
5  4  3         i=2, j=5,4,3
5  4            i=3, j=5,4
5               i=4, j=5

i is the row number (iterates) -> decrements
j is the column number (prints) -> repeats

'''
for i in range(6):
    for j in range(1,6-i):
        print(j, end =' ')
    print(end='\n')

'''
Output: (prints j)
1  2  3  4  5   i=0, j=1,2,3,4,5
1  2  3  4      i=1, j=1,2,3,4
1  2  3         i=2, j=1,2,3
1  2            i=3, j=1,2
1               i=4, j=1
                i=5, j=0

i is the row number (iterates) -> increments
j is the column number (prints) -> repeats


'''

# Equilateral Triangle Pattern

for i in range(5):
    print(' '*(5-i-1), end=' ') 
    # Can use (5-i) as well, which will give the same output but a bit aligned to the left
    for j in range(i+1):
        print(i, end =' ')
    print(end='\n')
    
'''
Output: (prints i)

        0             i=0, j=0
      1  1            i=1, j=0,1
     2  2  2          i=2, j=0,1,2
    3  3  3  3        i=3, j=0,1,2,3
   4  4  4  4  4      i=4, j=0,1,2,3,4

i is the row number (prints) -> repeats
j is the column number (iterates) -> increments

'''

# Square Hollow Pattern

for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4: # i=0,4 and j=0,4 -> first and last row and column
            print('*', end=" ")
        else:
            print(' ', end=" ")
    print(end='\n')

'''
Output:

* * * * * 
*       * 
*       * 
*       * 
* * * * * 

'''

# Hollow Triangle Pattern

for i in range(5):
    # print(' '*(5-i-1), end=' ') --> (for equilateral triangle)
    for j in range(i+1):
        if i==4 or i==j or j==0: # this makes it hollow
            print('*', end=' ')
        else:
            print(' ', end= ' ')
    print(end='\n')

'''
Output: (right-angled triangle)

* 
* * 
*   * 
*     * 
* * * * * 

Think j as y-axis and i as x-axis (on both sides),
i=4 and j=0 
and the line will be i=j

'''
for i in range(5):
    print(' '*(5-i-1), end=' ')
    for j in range(i+1):
        if i==4 or i==j or j==0: # this makes it hollow
            print('*', end=' ')
        else:
            print(' ', end= ' ')
    print(end='\n')

'''
Output: (equilateral triangle)

     * 
    * * 
   *   * 
  *     * 
 * * * * * 

Same as above but with spaces in between.

'''

for i in range(5,-1,-1):
    print(' '*(5-i), end=' ') # this condition is for converting inverted hollow right-angled triangle to inverted hollow equilateral triangle
    for j in range(i+1):
        if i==5 or j==0 or i==j: # this makes it hollow
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print(end='\n')

'''
Output: (Inverted equilateral hollow triangle)

 * * * * * * 
  *       * 
   *     * 
    *   * 
     * * 
      * 

'''

# Diamond Pattern

for i in range(4): # Equilateral triangle
    print(' '*(4-i), end=' ')
    for j in range(i+1):
        print('*', end=' ')
    print(end='\n')
for i in range(4,-1,-1): # Inverted equilateral triangle
    print(' '*(4-i), end=' ')
    for j in range(i+1):
        print('*', end=' ')
    print(end='\n')

'''
Output:

     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 

This is made by combining the inverted right-angled triangle and right-angled triangle patterns.

'''

# Diamond Hollow Pattern

for i in range(5):
    print(' '*(5-i-1), end=' ') # This makes the equilateral triangle
    for j in range(i+1):
        if i==5 or i==j or j==0: # This make the equilateral triangle hollow
            print('*', end=' ')
        else:
            print(' ', end= ' ')
    print(end='\n')
for i in range(4,-1,-1): # It is 4 instead of 5 because the last row is already printed
    print(' '*(5-i-1), end=' ') # This makes the inverted equilateral triangle
    for j in range(i+1):
        if i==5 or i==j or j==0: # This make the inverted equilateral triangle hollow
            print('*', end=' ')
        else:
            print(' ', end= ' ')
    print(end='\n')

'''
Output:

     * 
    * * 
   *   * 
  *     * 
 *       * 
 *       * 
  *     * 
   *   * 
    * * 
     * 



'''

# Reverse Number inverted equilateral triangle Pattern 


for i in range(5): # Outer loop controls the number of rows (5 rows in total)
    
    for j in range(i): # First inner loop: prints spaces to align the numbers to the right
        print(" ", end="")  # print a space without a newline

    for j in range(i + 1, 6): # Second inner loop: prints numbers starting from i+1 up to 5
        print(j, end=" ")  # print number with a space, no newline

    
    print()   # After printing each row, move to the next line


'''
Output:

1 2 3 4 5
 2 3 4 5
  3 4 5
   4 5
    5
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


i is the row number
j is the column number
k is the column number for the second half of the pattern


'''