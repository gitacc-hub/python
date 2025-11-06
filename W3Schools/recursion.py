# Recursion is a programming technique where a function calls itself either directly or indirectly
# to solve a problem by breaking it into smaller, simpler subproblems.

"""
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
# Recursion under the hood ( 7*6*5*4*3*2*1 )
print(factorial(8))
"""

"""
def sumRecursive(n):
    if n==1:
        return 1
    else:
        return n+sumRecursive(n-1)
print(sumRecursive(5))
"""

# Example 2: Fibonacci Sequence
"""
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(10))
"""