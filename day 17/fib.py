
# Program to find nth Fibonacci number using recursion

def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if _name_ == "_main_":
    n = 7
    print(f"{n}th Fibonacci number = {fibonacci(n)}")