text = " Hello, Python World! "
print("Original String:", repr(text))

# 1. strip() - removes whitespace from both ends
print("After strip():", text.strip())

# 2. lower() - converts to lowercase
print("lower():", text.lower())

# 3. upper() - converts to uppercase
print("upper():", text.upper())

# 4. replace() - replaces substring
print("replace():", text.replace("Python", "GitHub"))

# 5. split() - splits string into list
print("split():", text.split(","))

# 6. find() - returns index of substring (-1 if not found)
print("find('World'):", text.find("World"))

# 7. startswith() - checks prefix
print("startswith(' Hello'):", text.startswith(" Hello"))

# 8. endswith() - checks suffix
print("endswith('! '):", text.endswith("! "))

# 9. count() - counts occurrences of substring
print("count('o'):", text.count("o"))

# 10. isalpha() - checks if only alphabets
word = "Python"
print(f"isalpha() on '{word}':", word.isalpha())