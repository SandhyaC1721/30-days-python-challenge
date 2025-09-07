def rotate_list(lst, k):
    k = k % len(lst)  # handle rotation larger than list length
    return lst[-k:] + lst[:-k]
numbers = [1, 2, 3, 4, 5]

print("Original list:", numbers)
print("List rotated by 1:", rotate_list(numbers, 1))
print("List rotated by 2:", rotate_list(numbers, 2))
print("List rotated by 3:", rotate_list(numbers, 3))