x=100
y=200
z=300

if x==100:
    if y==200:
        if z==301:
            print("Yes it is 300")
    else:
        if y==210:
            print('Y is 200')
        else:
            print('Nothing')
'''
Since z != 300, it wont print -> Yes it is 300
thus it activates the next block i.e initialised by 'else'
In that block,
it will check if y=200. 
if true, it will print -> Y is 200
if false, it will print -> Nothing

'''


