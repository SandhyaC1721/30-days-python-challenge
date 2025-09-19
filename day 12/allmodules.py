import math
import random
import string
from datetime import datetime

# Math module
print("Square root of 25:", math.sqrt(25))
print("Factorial of 6:", math.factorial(6))

# Random module - password generator
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(12))
print("Generated Password:", password)

# Datetime module
now = datetime.now()
print("Current Date and Time:", now)