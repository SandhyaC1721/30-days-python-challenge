def factorial_for(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
# Call the function
num = int(input("Enter a number: "))
print("Factorial of", num, "is:", factorial_for(num))