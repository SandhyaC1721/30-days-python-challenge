def isValid(s):
    stack = []
    pair = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch in pair.values():
            stack.append(ch)
        elif ch in pair:
            if not stack or stack.pop() != pair[ch]:
                return False
    return not stack

# Example
print(isValid("{[()]}"))  # True
print(isValid("{[(])}"))  # False
