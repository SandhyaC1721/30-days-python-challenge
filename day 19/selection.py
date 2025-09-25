
# Selection Sort Implementation

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # swap
        arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == "_main_":
    data = [64, 25, 12, 22, 11]
    print("Original array:", data)
    selection_sort(data)
    print("Sorted array:", data)