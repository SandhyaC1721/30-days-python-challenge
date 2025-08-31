# Operator Precedence in Python

result1 = 2 + 3 * 4
print("2 + 3 * 4 =", result1)   # Multiplication happens first → 2 + 12 = 14

result2 = (2 + 3) * 4
print("(2 + 3) * 4 =", result2) # Parentheses first → 5 * 4 = 20

result3 = 2 ** 3 ** 2
print("2 ** 3 ** 2 =", result3) # Exponent is right-associative → 2 ** (3 ** 2) = 512

result4 = not 2 > 3 and 10 > 5
print("not 2 > 3 and 10 > 5 =", result4)  # not (False) and True → True