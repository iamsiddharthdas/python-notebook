
a = 0
b = 1
print(a)
print(b)

i = 1
while i <= 4:
    c = a + b
    print(c)
    a = b
    b = c
    i += 1
    

'''
Output pattern:(last 2 adds up)

Default
0
1

Generated 
0+1 i.e. 1 
1+(0+1) i.e. 2
(0+1) + [1+(0+1)] i.e. 3
[1+(0+1)] + {(0+1) + [1+(0+1)]} i.e 5

Final Output:
0
1
1
2
3
5


'''