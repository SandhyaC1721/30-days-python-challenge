num = int(input("Enter a number: "))
total = 0

while num > 0:
    digit = num % 10      # Get last digit
    total += digit        # Add it to total
    num //= 10            # Remove last digit

print("Sum of digits is:", total)