# Using List Comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares_list_comp = [x**2 for x in numbers]
print("Squares using List Comprehension:", squares_list_comp)

# Using Lambda Function with map()
squares_lambda = list(map(lambda x: x**2, numbers))
print("Squares using Lambda Function:", squares_lambda)