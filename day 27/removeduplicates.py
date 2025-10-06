def remove_duplicates(lst):
    return list(set(lst))   # convert to set (removes duplicates), then back to list
numbers = [1, 2, 2, 3, 4, 4, 5, 1, 6]
print("Original list:", numbers)
print("After removing duplicates:", remove_duplicates(numbers))