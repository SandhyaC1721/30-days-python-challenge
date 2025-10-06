
stack = []  # empty list for stack

# Push (add element)
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack after pushes:", stack)

# Pop (remove element)
stack.pop()
print("Stack after pop:", stack)

# Peek (see top element)
print("Top element:", stack[-1])

# Check if empty
print("Is stack empty?", len(stack) == 0)