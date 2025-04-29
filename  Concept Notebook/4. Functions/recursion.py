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




# Example:
# Print the multiplication table of a number using basic recursion


def table(num,i):
    if i>10: # Base case
        return
    print(num,'X',i,'=',num*i)
    
    i = i+1 # Recursive case
    table(num,i)
table(5,1)

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

'''
Function with Backtracking: Current calls -> previous calls

def backtrack(choices, solution):
    if is_solution(solution):
        process_solution(solution)
    else:
        for choice in choices:
            if is_valid(choice, solution):
                solution.append(choice)
                backtrack(choices, solution)
                solution.pop()
                


Here's how it works:
1. The function checks if the current solution is valid.
2. If it is, it processes the solution.
3. If not, it iterates through the choices.
4. For each choice, it checks if it's valid.
5. If valid, it adds the choice to the solution and calls itself recursively.

Example:

'''

# Factorial of a number using recursion (backtracking)

def factorial(n):
    if n == 0 or n == 1: # Base case
        return 1
    else: # Recursive case
        return n * factorial(n - 1) # Recursive call with modified parameter

'''

Backtracking: Current calls -> previous calls

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

# Fibonacci series using recursion

def fib(n):
    if n <= 1: # Base case
        return n
    return fib(n-1) + fib(n-2) # Recursive case

'''
+------------------+-----------------------------------------+
|  Function Call   |          Return / Evaluation            |
+------------------+-----------------------------------------+
| fib(0)           | → 0 (base case)                         |
| fib(1)           | → 1 (base case)                         |
| fib(2)           | → fib(1) + fib(0) = 1 + 0 = 1           |
| fib(1)           | → 1 (base case)                         |
| fib(3)           | → fib(2) + fib(1) = 1 + 1 = 2           |
| fib(2)           | → fib(1) + fib(0) = 1 + 0 = 1           |
| fib(4)           | → fib(3) + fib(2) = 2 + 1 = 3           |
| fib(1)           | → 1 (base case)                         |
| fib(5)           | → fib(4) + fib(1) = 3 + 1 = 5           |
+------------------+-----------------------------------------+
| main()           | ← returns 5                             |
+------------------+-----------------------------------------+


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
    if b==0:
        return 1
    return a*power(a,b-1)

print((power(5,3)))

'''
Output:

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