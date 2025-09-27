def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i

# Example usage:
print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]