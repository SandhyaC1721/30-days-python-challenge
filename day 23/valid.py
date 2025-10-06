def isPalindrome(s):
    filtered = [c.lower() for c in s if c.isalnum()]
    return filtered == filtered[::-1]

# Example usage:
print(isPalindrome("A man, a plan, a canal: Panama"))  # Output: True