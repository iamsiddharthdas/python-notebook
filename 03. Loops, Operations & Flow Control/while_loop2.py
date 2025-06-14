
num=0
while i<25:
    num=num+i
    i=i+5
print("my num is",num)

'''
i=0, num = num+i = 0
i=5, num = num+i = 5
i=10, num = num+i = 15
i=15, num = num+i = 30
i=20, num = num+i = 50
i=25, num = num+i = 75



output:
0
5
15
30
50
75

pattern:
0
0+5
0+5+10
0+5+10+15
0+5+10+15+20
0+5+10+15+20+25

'''