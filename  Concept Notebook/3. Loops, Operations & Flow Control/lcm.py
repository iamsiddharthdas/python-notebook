x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))


if x > y and x > z:
    greater = x
elif y > x and y > z:
    greater = y
else:
    greater = z


while True:
    if greater % x == 0 and greater % y == 0 and greater % z == 0:
        print("LCM is", greater)
        break
    else:
        greater += 1
        

