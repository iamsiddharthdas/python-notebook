num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = int(num/10)

if original == reverse:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")