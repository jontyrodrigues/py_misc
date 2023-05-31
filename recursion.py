# an app which uses recursion to calculate the factorial of a number

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(100))
