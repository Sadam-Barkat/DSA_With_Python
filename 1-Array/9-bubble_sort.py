def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):  # Number of passes
        swapped = False  # Optimization: Check if swapping happens
        for j in range(n - i - 1):  # Last i elements are already sorted
            if arr[j] > arr[j + 1]:  # Swap if elements are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # If no swaps in a pass, array is already sorted
            break
    return arr

# Example Usage
arr = [5, 3, 8, 6, 2]
print(bubble_sort(arr))  # Output: [2, 3, 5, 6, 8]
