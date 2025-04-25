'''
Return Function 
1. Breaks the function 
2. Prints the return value


Example:
def prime_no(num):
    count = 0
    i= 1
    while i <= num:
        if num % i == 0:
            count += 1
        i += 1
    if count == 2:
        return num, "is a prime number"
    else:
        return num, "is not a prime number"

'''

def prime_no(num):
    
    count = 0
    i= 1
    while i <= num:
        if num % i == 0:
            count += 1
        i += 1
    if count == 2:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
        
prime_no(5) # prints 5 is a prime number
prime_no(4) # prints 4 is not a prime number

# The function prime_no checks if a number is prime or not.

def table(num):
    for i in range(1,11):
        print(num,"x",i,"=",num*i)

table(12)

# The function table prints the multiplication table of a given number.

def find_lcm(x, y, z):
    greater = max(x, y, z)

    while True:
        if greater % x == 0 and greater % y == 0 and greater % z == 0:
            return greater
        greater += 1


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

lcm = find_lcm(x, y, z)
print("LCM is", lcm)

# The function find_lcm finds the least common multiple of three numbers.

def print_pattern():
    choice = input("Enter 1 for square pattern, 2 for triangle pattern: ")

    if choice == '1':
        for i in range(5):
            for j in range(5):
                print("*", end=" ")
            print(end="\n")

    elif choice == '2':
        for i in range(5):
            print(' '*(5-i-1), end=' ')
            for j in range(i+1):
                print('*', end=' ')

            print(end='\n')

    else:
        print("Invalid input! Please enter 1 or 2.")


print_pattern()

# The function print_pattern prints a square or triangle pattern based on user input.

def fibonacci_sequence(n):
    a = 0
    b = 1
    print(a)
    print(b)

    i = 1
    while i <= 5:
        c = a + b
        print(c)
        a = b
        b = c
        i += 1

fibonacci_sequence(6)

# The function fibonacci_sequence generates the Fibonacci sequence up to the 5 terms.

