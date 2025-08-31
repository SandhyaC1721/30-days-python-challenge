# Identity Operators in Python

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("a =", a)
print("b =", b)
print("c =", c)

# 'is' checks if two variables refer to the same object
print("a is b:", a is b)       
print("a is c:", a is c)       
# 'is not' checks if two variables refer to different objects
print("a is not b:", a is not b) 
print("a is not c:", a is not c) 