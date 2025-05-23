x = int(input('Enter a number '))
y = int(input('Enter a number '))
z = int(input('Enter a number '))

less = min(x,y,z)

while True:
    if x % less == 0 and y % less == 0 and z % less == 0:
        print('HCF is',less)
        break
    else:
        less -= 1
        
    