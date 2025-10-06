def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    count = {}
    
    # Count characters in s1
    for char in s1:
        count[char] = count.get(char, 0) + 1
    
    # Subtract counts using s2
    for char in s2:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False
    
    return True

# Example
print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "bello"))    # False
