# Program to find factorial using recursion

def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    return n * factorial(n - 1)


if _name_ == "_main_":
    num = 5
    print(f"Factorial of {num} = {factorial(num)}")