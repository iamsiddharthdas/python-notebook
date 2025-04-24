'''
Nested for loop:
Here, we are using two for loops

'''
for i in range(0,3,1):
    for j in range(0,3,1):
        print(i,j)

'''
Output:
0 0
0 1
0 2
0 3
0 4
1 0
1 1
1 2
1 3
1 4
2 0
2 1
2 2
2 3
2 4
3 0
3 1
3 2
3 3
3 4


Explanation:
1. The outer loop iterates from 0 to 2 (3 iterations)
2. The inner loop cycles through the range from 0 to 2 (3 iterations) and increments j
3. The increment stops when j reaches 3
4. The inner loop prints the value of i and j
5. The outer loop increments i and the inner loop starts again
6. The process continues until the outer loop reaches its limit


'''

for i in range(7,0,-3):
    for j in range(0,3,1):
        print(i,j)
        
'''
Output:
7 0
7 1
7 2
4 0
4 1
4 2
1 0
1 1
1 2
'''

for i in range(4,6,1):
    for j in range(10,12,1):
        for k in range(1,3,1):
            print(i,j,k)
'''
Output:
4 10 1
4 10 2
4 11 1
4 11 2
5 10 1
5 10 2
5 11 1
5 11 2

'''