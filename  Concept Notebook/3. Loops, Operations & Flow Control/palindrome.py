num = int(input("Enter a number: "))
temp = num

reverse = 0

while temp > 0:
    remainder = temp % 10
    reverse = reverse * 10 + remainder
    temp = temp//10

'''
Divide the num (stored in temp) by 10

Quotient will store in temp
Remainder will store in remainder

'''

if num == reverse:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")