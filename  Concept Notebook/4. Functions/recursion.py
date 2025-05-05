'''
Recursion is when a function calls itself to solve a problem.

Basic format of a recursive function:
def recursive_function(parameters): # Base case
    if base_case_condition:
        return base_case_value
    else: # Recursive case
        return recursive_function(modified_parameters)

The base case is the condition that stops the recursion. It prevents infinite recursion.
The recursive case is the part of the function that calls itself with modified parameters.

Example:
def countdown(n):
    if n == 0:
        print("Blast off!")
        return
    print(n)
    countdown(n - 1)
    
Output for countdown(5):
5
4
3
2
1
Blast off!
'''


#### 1. Linear Recursion ####

# Print the multiplication table of a number using basic recursion


def table(num,i):
    
    if i>10:
        return
    print(num,'X',i,'=',num*i)
    i = i+1
    table(num,i)
    
num = int(input("Enter a number to print its multiplication table: "))
table(num,1)

'''
Explanation:
1. The function `table` takes two parameters: `num` (the number for which the table is to be printed) and `i` (the current multiplier).
2. The base case checks if `i` is greater than 10. If it is, the function returns and stops further execution.
3. If `i` is not greater than 10, it prints the multiplication of `num` and `i`.
4. The function then increments `i` by 1 and calls itself with the updated value of `i`.

Output:
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15..... till 5 X 10 = 50
'''

# Factorial of a number using recursion (backtracking)

def factorial(n):
    if n == 0 or n == 1: # Base case
        return 1
    else: # Recursive case
        return n * factorial(n - 1) # Recursive call with modified parameter

'''

Backtracking: Return statement is used.

For n = 7

+-------------------+---------------------------------------------+
|   Function Call   |          Return / Evaluation                |
+-------------------+---------------------------------------------+
| factorial(1)      | → 1                                         |
| factorial(2)      | → 2 * factorial(1) = 2 * 1 = 2              |
| factorial(3)      | → 3 * factorial(2) = 3 * 2 = 6              |
| factorial(4)      | → 4 * factorial(3) = 4 * 6 = 24             |
| factorial(5)      | → 5 * factorial(4) = 5 * 24 = 120           |
| factorial(6)      | → 6 * factorial(5) = 6 * 120 = 720          |
| factorial(7)      | → 7 * factorial(6) = 7 * 720 = 5040         |
+-------------------+---------------------------------------------+
| main()            | ← returns 5040                              |
+-------------------+---------------------------------------------+

'''


def sum_natural(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural(n - 1)

print(sum_natural(5))

'''
+-----------------------+------------------------------------+
|    Function Call      |         Return / Evaluation        |
+-----------------------+------------------------------------+
| sum_natural(0)        | → 0                                |
| sum_natural(1)        | → 1 + sum_natural(0) = 1 + 0 = 1   |
| sum_natural(2)        | → 2 + sum_natural(1) = 2 + 1 = 3   |
| sum_natural(3)        | → 3 + sum_natural(2) = 3 + 3 = 6   |
| sum_natural(4)        | → 4 + sum_natural(3) = 4 + 6 = 10  |
| sum_natural(5)        | → 5 + sum_natural(4) = 5 + 10 = 15 |
+-----------------------+------------------------------------+
| main()                | ← returns 15                       |
+-----------------------+------------------------------------+


'''
def power(a,b):
    
    if b == 0:
        return 1
    else:
        return a*power(a,b-1)
        
a = int(input('Base: '))
b = int(input('Exponent: '))

print((power(a,b)))

'''
Output:
a = 5
b = 3

+--------------------+----------------------------------+
|   Function Call    |        Return / Evaluation       |
+--------------------+----------------------------------+
| power(5, 0)        | → 1                              |
| power(5, 1)        | → 5 * power(5, 0) = 5 * 1 = 5    |
| power(5, 2)        | → 5 * power(5, 1) = 5 * 5 = 25   |
| power(5, 3)        | → 5 * power(5, 2) = 5 * 25 = 125 |
+--------------------+----------------------------------+
| main()             | ← returns 125                    |
+--------------------+----------------------------------+



'''

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

print(gcd(48,18))

'''

+------------------+----------------------------------+
|  Function Call   |     Return / Evaluation          |
+------------------+----------------------------------+
| gcd(48, 18)      | → gcd(18, 48 % 18) = gcd(18, 12) |
| gcd(18, 12)      | → gcd(12, 18 % 12) = gcd(12, 6)  |
| gcd(12, 6)       | → gcd(6, 12 % 6) = gcd(6, 0)     |
| gcd(6, 0)        | → 6 (base case reached)          |
+------------------+----------------------------------+
| main()           | ← returns 6                      |
+------------------+----------------------------------+


'''

def product_of_digit(n):
    if n<10:
        return n
    return(n%10)* product_of_digit(n//10)
    # n%10 - Remainder 
    # n//10 - Quotient
    
print(product_of_digit(563))

'''
+------------------------+--------------------------------------------+
|    Function Call       |        Return / Evaluation                 |
+------------------------+--------------------------------------------+
| product_of_digit(563)  | → (563 % 10) * product_of_digit(563 // 10) |
|                        | → 3 * product_of_digit(56)                 |
| product_of_digit(56)   | → (56 % 10) * product_of_digit(56 // 10)   |
|                        | → 6 * product_of_digit(5)                  |
| product_of_digit(5)    | → 5 (base case reached)                    |
+------------------------+--------------------------------------------+
| Evaluation Rollback    | 6 * 5 = 30 (from product_of_digit(56))     | 
|                        | 3 * 30 = 90 (from product_of_digit(563))   |
+------------------------+--------------------------------------------+
| main() (print)         | ← prints 90                                |
+------------------------+--------------------------------------------+


'''

# Sum of digits of a number
def sod(n):
    if n<10:
        return n
    else:
        return n%10 + sod(n//10)
        # n%10 - Remainder
        # n//10 - Quotient

sod(1234)

'''
+------------------------+--------------------------------------------+
|    Function Call       |        Return / Evaluation                 |
+------------------------+--------------------------------------------+
| sod(1234)              | → (1234 % 10) + sod(1234 // 10)            |
|                        | → 4 + sod(123)                             |
| sod(123)               | → (123 % 10) + sod(123 // 10)              |
|                        | → 3 + sod(12)                              |
| sod(12)                | → (12 % 10) + sod(12 // 10)                |
|                        | → 2 + sod(1)                               |
| sod(1)                 | → 1 (base case reached)                    |
+------------------------+--------------------------------------------+
| Evaluation Rollback    | 2 + 1 = 3 (from sod(12))                   |
|                        | 3 + 3 = 6 (from sod(123))                  |
|                        | 4 + 6 = 10 (from sod(1234))                |
+------------------------+--------------------------------------------+
| main() (print)         | ← prints 10                                |
+------------------------+--------------------------------------------+

'''
# Reverse the digits of a number 
def reverse(n, rev=0):
    if n == 0:
        return rev
    else:
        return reverse(n // 10, rev * 10 + n % 10)
        #n%10 - Remainder (last digit)
        #n//10 - Quotient (all digits except last)

n = int(input("Enter a number: "))  
print(reverse(n))  

'''
for 

n = 1234

+----------------------------+------------------------------------------------+
|     Function Call          |         Return / Evaluation                    | 
+----------------------------+------------------------------------------------+
| reverse(1234, 0)           | → reverse(123, 0 * 10 + 4) = reverse(123, 4)   |
| reverse(123, 4)            | → reverse(12, 4 * 10 + 3) = reverse(12, 43)    |
| reverse(12, 43)            | → reverse(1, 43 * 10 + 2) = reverse(1, 432)    |
| reverse(1, 432)            | → reverse(0, 432 * 10 + 1) = reverse(0, 4321)  |
| reverse(0, 4321)           | → 4321 (base case reached)                     |
+----------------------------+------------------------------------------------+
| Evaluation Rollback        | Returns 4321 upward                            |
+----------------------------+------------------------------------------------+
| main() (print)             | ← prints 4321                                  |
+----------------------------+------------------------------------------------+

'''

#### Binary Recursion ####

# Two function calls:

def fun(x):
    if x>0:
        print(x)
        fun(x-1)
        fun(x-2)
        
fun(4)

'''

fun(4)
├── S1: print(4)                         # OUTPUT 1
├── F1: fun(3)
│   ├── S1: print(3)                     # OUTPUT 2
│   ├── F1: fun(2)
│   │   ├── S1: print(2)                 # OUTPUT 3
│   │   ├── F1: fun(1)
│   │   │   ├── S1: print(1)             # OUTPUT 4
│   │   │   ├── F1: fun(0) ✘
│   │   │   └── F2: fun(-1) ✘
│   │   └── F2: fun(0) ✘
│   └── F2: fun(1)
│       ├── S1: print(1)                 # OUTPUT 5
│       ├── F1: fun(0) ✘
│       └── F2: fun(-1) ✘
└── F2: fun(2)
    ├── S1: print(2)                     # OUTPUT 6
    ├── F1: fun(1)
    │   ├── S1: print(1)                 # OUTPUT 7
    │   ├── F1: fun(0) ✘
    │   └── F2: fun(-1) ✘
    └── F2: fun(0) ✘


Output :
4
3
2
1
1
2
1


'''
def fun(x):
    if x>0:
        fun(x-1)
        print(x)
        fun(x-2)
        
fun(5)

'''


fun(5)
├── F1: fun(4)
│   ├── F1: fun(3)
│   │   ├── F1: fun(2)
│   │   │   ├── F1: fun(1)
│   │   │   │   ├── F1: fun(0) ✘
│   │   │   │   ├── S1: print(1)         # OUTPUT 1
│   │   │   │   └── F2: fun(-1) ✘
│   │   │   ├── S1: print(2)             # OUTPUT 2
│   │   │   └── F2: fun(0) ✘
│   │   ├── S1: print(3)                 # OUTPUT 3
│   │   └── F2: fun(1)
│   │       ├── F1: fun(0) ✘
│   │       ├── S1: print(1)             # OUTPUT 4
│   │       └── F2: fun(-1) ✘
│   ├── S1: print(4)                     # OUTPUT 5
│   └── F2: fun(2)
│       ├── F1: fun(1)
│       │   ├── F1: fun(0) ✘
│       │   ├── S1: print(1)             # OUTPUT 6
│       │   └── F2: fun(-1) ✘
│       ├── S1: print(2)                 # OUTPUT 7
│       └── F2: fun(0) ✘
├── S1: print(5)                         # OUTPUT 8
└── F2: fun(3)
    ├── F1: fun(2)
    │   ├── F1: fun(1)
    │   │   ├── F1: fun(0) ✘
    │   │   ├── S1: print(1)             # OUTPUT 9
    │   │   └── F2: fun(-1) ✘
    │   ├── S1: print(2)                 # OUTPUT 10
    │   └── F2: fun(0) ✘
    ├── S1: print(3)                     # OUTPUT 11
    └── F2: fun(1)
        ├── F1: fun(0) ✘
        ├── S1: print(1)                 # OUTPUT 12
        └── F2: fun(-1) ✘

Final printed output:
1
2
3
1
4
1
2
5
1
2
3
1

'''
def fun(x):
    if x>0:
        fun(x-1)
        fun(x-2)
        print(x)
        
fun(5)

'''


fun(5)
├── F1: fun(4)
│   ├── F1: fun(3)
│   │   ├── F1: fun(2)
│   │   │   ├── F1: fun(1)
│   │   │   │   ├── F1: fun(0) ✘
│   │   │   │   ├── F2: fun(-1) ✘
│   │   │   │   └── S1: print(1)         # OUTPUT 1
│   │   │   ├── F2: fun(0) ✘
│   │   │   └── S1: print(2)             # OUTPUT 2
│   │   ├── F2: fun(1)
│   │   │   ├── F1: fun(0) ✘
│   │   │   ├── F2: fun(-1) ✘
│   │   │   └── S1: print(1)             # OUTPUT 3
│   │   └── S1: print(3)                 # OUTPUT 4
│   ├── F2: fun(2)
│   │   ├── F1: fun(1)
│   │   │   ├── F1: fun(0) ✘
│   │   │   ├── F2: fun(-1) ✘
│   │   │   └── S1: print(1)             # OUTPUT 5
│   │   ├── F2: fun(0) ✘
│   │   └── S1: print(2)                 # OUTPUT 6
│   └── S1: print(4)                     # OUTPUT 7
├── F2: fun(3)
│   ├── F1: fun(2)
│   │   ├── F1: fun(1)
│   │   │   ├── F1: fun(0) ✘
│   │   │   ├── F2: fun(-1) ✘
│   │   │   └── S1: print(1)             # OUTPUT 8
│   │   ├── F2: fun(0) ✘
│   │   └── S1: print(2)                 # OUTPUT 9
│   ├── F2: fun(1)
│   │   ├── F1: fun(0) ✘
│   │   ├── F2: fun(-1) ✘
│   │   └── S1: print(1)                 # OUTPUT 10
│   └── S1: print(3)                     # OUTPUT 11
└── S1: print(5)                         # OUTPUT 12

Output:
1
2
1
3
1
2
4
1
2
1
3
5

'''

# Three function calls:

def fun(x,y,z):
    if x>0:
        fun(x-2,y,z)
        y=y+20
        fun(x-1,y,z)
        z=z*2
        print(x,y,z)
        fun(x-2,y,z)
    
fun(4,5,6)

'''
fun(4, 5, 6)
├── F1: fun(2, 5, 6)
│   ├── F1: fun(0, 5, 6) ✘
│   ├── y = 5 + 20 = 25
│   ├── F2: fun(1, 25, 6)
│   │   ├── F1: fun(-1, 25, 6) ✘
│   │   ├── y = 25 + 20 = 45
│   │   ├── F2: fun(0, 45, 6) ✘
│   │   ├── z = 6 * 2 = 12
│   │   ├── S1: print(1, 45, 12)         → OUTPUT 1
│   │   └── F3: fun(-1, 45, 12) ✘
│   ├── z = 6 * 2 = 12
│   ├── S1: print(2, 25, 12)             → OUTPUT 2
│   └── F3: fun(0, 25, 12) ✘

├── y = 5 + 20 = 25
├── F2: fun(3, 25, 6)
│   ├── F1: fun(1, 25, 6)
│   │   ├── F1: fun(-1, 25, 6) ✘
│   │   ├── y = 25 + 20 = 45
│   │   ├── F2: fun(0, 45, 6) ✘
│   │   ├── z = 6 * 2 = 12
│   │   ├── S1: print(1, 45, 12)         → OUTPUT 3
│   │   └── F3: fun(-1, 45, 12) ✘
│   ├── y = 25 + 20 = 45
│   ├── F2: fun(2, 45, 6)
│   │   ├── F1: fun(0, 45, 6) ✘
│   │   ├── y = 45 + 20 = 65
│   │   ├── F2: fun(1, 65, 6)
│   │   │   ├── F1: fun(-1, 65, 6) ✘
│   │   │   ├── y = 65 + 20 = 85
│   │   │   ├── F2: fun(0, 85, 6) ✘
│   │   │   ├── z = 6 * 2 = 12
│   │   │   ├── S1: print(1, 85, 12)     → OUTPUT 4
│   │   │   └── F3: fun(-1, 85, 12) ✘
│   │   ├── z = 6 * 2 = 12
│   │   ├── S1: print(2, 65, 12)         → OUTPUT 5
│   │   └── F3: fun(0, 65, 12) ✘
│   ├── z = 6 * 2 = 12
│   ├── S1: print(3, 45, 12)             → OUTPUT 6
│   └── F3: fun(1, 45, 12)
│       ├── F1: fun(-1, 45, 12) ✘
│       ├── y = 45 + 20 = 65
│       ├── F2: fun(0, 65, 12) ✘
│       ├── z = 12 * 2 = 24
│       ├── S1: print(1, 65, 24)         → OUTPUT 7
│       └── F3: fun(-1, 65, 24) ✘

├── z = 6 * 2 = 12
├── S1: print(4, 25, 12)                 → OUTPUT 8
└── F3: fun(2, 25, 12)
    ├── F1: fun(0, 25, 12) ✘
    ├── y = 25 + 20 = 45
    ├── F2: fun(1, 45, 12)
    │   ├── F1: fun(-1, 45, 12) ✘
    │   ├── y = 45 + 20 = 65
    │   ├── F2: fun(0, 65, 12) ✘
    │   ├── z = 12 * 2 = 24
    │   ├── S1: print(1, 65, 24)         → OUTPUT 9
    │   └── F3: fun(-1, 65, 24) ✘
    ├── z = 12 * 2 = 24
    ├── S1: print(2, 45, 24)             → OUTPUT 10
    └── F3: fun(0, 45, 24) ✘

Output:

1 45 12
2 25 12
1 45 12
1 85 12
2 65 12
3 45 12
1 65 24
4 25 12
1 65 24
2 45 24


'''

def fun(x, y, z):
    if x > 0:
        z = z * 2
        fun(x - 2, y, z)
        y = y + 20
        fun(x - 1, y, z)
        print(x, y, z)
        fun(x - 2, y, z)
        
fun(4,5,6)
'''
fun(4, 5, 6)
├── S1: z = 6 * 2 = 12
├── F1: fun(2, 5, 12)
│   ├── S1: z = 12 * 2 = 24
│   ├── F1: fun(0, 5, 24) ✘
│   ├── y = 5 + 20 = 25
│   ├── F2: fun(1, 25, 24)
│   │   ├── S1: z = 24 * 2 = 48
│   │   ├── F1: fun(-1, 25, 48) ✘
│   │   ├── y = 25 + 20 = 45
│   │   ├── F2: fun(0, 45, 48) ✘
│   │   ├── S2: print(1, 45, 48)         → OUTPUT 1
│   │   └── F3: fun(-1, 45, 48) ✘
│   ├── S2: print(2, 25, 24)             → OUTPUT 2
│   └── F3: fun(0, 25, 24) ✘

├── y = 5 + 20 = 25
├── F2: fun(3, 25, 12)
│   ├── S1: z = 12 * 2 = 24
│   ├── F1: fun(1, 25, 24)
│   │   ├── S1: z = 24 * 2 = 48
│   │   ├── F1: fun(-1, 25, 48) ✘
│   │   ├── y = 25 + 20 = 45
│   │   ├── F2: fun(0, 45, 48) ✘
│   │   ├── S2: print(1, 45, 48)         → OUTPUT 3
│   │   └── F3: fun(-1, 45, 48) ✘
│   ├── y = 25 + 20 = 45
│   ├── F2: fun(2, 45, 24)
│   │   ├── S1: z = 24 * 2 = 48
│   │   ├── F1: fun(0, 45, 48) ✘
│   │   ├── y = 45 + 20 = 65
│   │   ├── F2: fun(1, 65, 48)
│   │   │   ├── S1: z = 48 * 2 = 96
│   │   │   ├── F1: fun(-1, 65, 96) ✘
│   │   │   ├── y = 65 + 20 = 85
│   │   │   ├── F2: fun(0, 85, 96) ✘
│   │   │   ├── S2: print(1, 85, 96)     → OUTPUT 4
│   │   │   └── F3: fun(-1, 85, 96) ✘
│   │   ├── S2: print(2, 65, 48)         → OUTPUT 5
│   │   └── F3: fun(0, 65, 48) ✘
│   ├── S2: print(3, 45, 24)             → OUTPUT 6
│   └── F3: fun(1, 45, 24)
│       ├── S1: z = 24 * 2 = 48
│       ├── F1: fun(-1, 45, 48) ✘
│       ├── y = 45 + 20 = 65
│       ├── F2: fun(0, 65, 48) ✘
│       ├── S2: print(1, 65, 48)         → OUTPUT 7
│       └── F3: fun(-1, 65, 48) ✘

├── S2: print(4, 25, 12)                 → OUTPUT 8
└── F3: fun(2, 25, 12)
    ├── S1: z = 12 * 2 = 24
    ├── F1: fun(0, 25, 24) ✘
    ├── y = 25 + 20 = 45
    ├── F2: fun(1, 45, 24)
    │   ├── S1: z = 24 * 2 = 48
    │   ├── F1: fun(-1, 45, 48) ✘
    │   ├── y = 45 + 20 = 65
    │   ├── F2: fun(0, 65, 48) ✘
    │   ├── S2: print(1, 65, 48)         → OUTPUT 9
    │   └── F3: fun(-1, 65, 48) ✘
    ├── S2: print(2, 45, 24)             → OUTPUT 10
    └── F3: fun(0, 45, 24) ✘


Output:
1 45 48
2 25 24
1 45 48
1 85 96
2 65 48
3 45 24
1 65 48
4 25 12
1 65 48
2 45 24

'''
# Fibonacci series 

def fib(n):
    if n <= 1: # Base case (0,1)
        return n
    return fib(n-1) + fib(n-2) # Recursive case
for i in range(8):
    print((fib(i)))

'''
fib(0) → 0                            # 1st

fib(1) → 1                            # 2nd

fib(2)
├── fib(1) → 1
├── fib(0) → 0
└── return 1 + 0 = 1                  # 3rd

fib(3)
├── fib(2)
│   ├── fib(1) → 1
│   ├── fib(0) → 0
│   └── return 1 + 0 = 1
├── fib(1) → 1
└── return 1 + 1 = 2                  # 4th

fib(4)
├── fib(3)
│   ├── fib(2)
│   │   ├── fib(1) → 1
│   │   ├── fib(0) → 0
│   │   └── return 1 + 0 = 1
│   ├── fib(1) → 1
│   └── return 1 + 1 = 2
├── fib(2)
│   ├── fib(1) → 1
│   ├── fib(0) → 0
│   └── return 1 + 0 = 1
└── return 2 + 1 = 3                  # 5th

fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2)
│   │   │   ├── fib(1) → 1
│   │   │   ├── fib(0) → 0
│   │   │   └── return 1 + 0 = 1
│   │   ├── fib(1) → 1
│   │   └── return 1 + 1 = 2
│   ├── fib(2)
│   │   ├── fib(1) → 1
│   │   ├── fib(0) → 0
│   │   └── return 1 + 0 = 1
│   └── return 2 + 1 = 3
├── fib(3)
│   ├── fib(2)
│   │   ├── fib(1) → 1
│   │   ├── fib(0) → 0
│   │   └── return 1 + 0 = 1
│   ├── fib(1) → 1
│   └── return 1 + 1 = 2
└── return 3 + 2 = 5                  # 6th

fib(6)
├── fib(5)
│   ├── fib(4)
│   │   ├── fib(3)
│   │   │   ├── fib(2)
│   │   │   │   ├── fib(1) → 1
│   │   │   │   ├── fib(0) → 0
│   │   │   │   └── return 1 + 0 = 1
│   │   │   ├── fib(1) → 1
│   │   │   └── return 1 + 1 = 2
│   │   ├── fib(2)
│   │   │   ├── fib(1) → 1
│   │   │   ├── fib(0) → 0
│   │   │   └── return 1 + 0 = 1
│   │   └── return 2 + 1 = 3
│   ├── fib(3)
│   │   ├── fib(2)
│   │   │   ├── fib(1) → 1
│   │   │   ├── fib(0) → 0
│   │   │   └── return 1 + 0 = 1
│   │   ├── fib(1) → 1
│   │   └── return 1 + 1 = 2
│   └── return 3 + 2 = 5
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2)
│   │   │   ├── fib(1) → 1
│   │   │   ├── fib(0) → 0
│   │   │   └── return 1 + 0 = 1
│   │   ├── fib(1) → 1
│   │   └── return 1 + 1 = 2
│   ├── fib(2)
│   │   ├── fib(1) → 1
│   │   ├── fib(0) → 0
│   │   └── return 1 + 0 = 1
│   └── return 2 + 1 = 3
└── return 5 + 3 = 8                  # 7th

fib(7)
├── fib(6)
│   ├── fib(5)
│   │   ├── fib(4)
│   │   │   ├── fib(3)
│   │   │   │   ├── fib(2)
│   │   │   │   │   ├── fib(1) → 1
│   │   │   │   │   ├── fib(0) → 0
│   │   │   │   │   └── return 1 + 0 = 1
│   │   │   │   ├── fib(1) → 1
│   │   │   │   └── return 1 + 1 = 2
│   │   │   ├── fib(2)
│   │   │   │   ├── fib(1) → 1
│   │   │   │   ├── fib(0) → 0
│   │   │   │   └── return 1 + 0 = 1
│   │   │   └── return 2 + 1 = 3
│   │   ├── fib(3)
│   │   │   ├── fib(2)
│   │   │   │   ├── fib(1) → 1
│   │   │   │   ├── fib(0) → 0
│   │   │   │   └── return 1 + 0 = 1
│   │   │   ├── fib(1) → 1
│   │   │   └── return 1 + 1 = 2
│   │   └── return 3 + 2 = 5
│   ├── fib(4)
│   │   ├── fib(3)
│   │   │   ├── fib(2)
│   │   │   │   ├── fib(1) → 1
│   │   │   │   ├── fib(0) → 0
│   │   │   │   └── return 1 + 0 = 1
│   │   │   ├── fib(1) → 1
│   │   │   └── return 1 + 1 = 2
│   │   ├── fib(2)
│   │   │   ├── fib(1) → 1
│   │   │   ├── fib(0) → 0
│   │   │   └── return 1 + 0 = 1
│   │   └── return 2 + 1 = 3
│   └── return 5 + 3 = 8
├── fib(5)
│   ├── fib(4)
│   │   ├── fib(3)
│   │   │   ├── fib(2)
│   │   │   │   ├── fib(1) → 1
│   │   │   │   ├── fib(0) → 0
│   │   │   │   └── return 1 + 0 = 1
│   │   │   ├── fib(1) → 1
│   │   │   └── return 1 + 1 = 2
│   │   ├── fib(2)
│   │   │   ├── fib(1) → 1
│   │   │   ├── fib(0) → 0
│   │   │   └── return 1 + 0 = 1
│   │   └── return 2 + 1 = 3
│   ├── fib(3)
│   │   ├── fib(2)
│   │   │   ├── fib(1) → 1
│   │   │   ├── fib(0) → 0
│   │   │   └── return 1 + 0 = 1
│   │   ├── fib(1) → 1
│   │   └── return 1 + 1 = 2
│   └── return 3 + 2 = 5
└── return 8 + 5 = 13                 # 8th 

Output:

0
1
1
2
3
5
8
13


'''



"""

KEY POINTS OF DIFFERENCE:


| Feature              | Linear Recursion            | Binary Recursion             |
|----------------------|-----------------------------|------------------------------|
| Recursive Calls/Step | 1                           | 2                            |
| Structure            | Straight line (depth)       | Tree (depth and width)       |
| Example              | Factorial, Sum of List      | Fibonacci, Binary Tree       |
| Memory Use           | Less (simpler stack)        | More (branches multiply)     |
| Performance          | Faster (often O(n))         | Slower if not optimized      |

"""

