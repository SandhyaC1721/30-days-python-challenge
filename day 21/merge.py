def merge(nums1, m, nums2, n):
    i, j, k = m-1, n-1, m+n-1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

# Example usage:
arr1 = [1,2,3,0,0,0]
merge(arr1, 3, [2,5,6], 3)
print(arr1)  # Output: [1,2,2,3,5,6]