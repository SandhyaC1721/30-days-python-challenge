# Program to find sum of first n natural numbers using recursion

def sum_n(n):
    if n == 0:   # base case
        return 0
    return n + sum_n(n - 1)


if __name__== "_main_":
    n = 10
    print(f"Sum of first {n} numbers = {sum_n(n)}")