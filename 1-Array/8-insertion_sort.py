def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):  # Start from the second element
        key = arr[i]
        j = i
        for j in range(i, 0, -1):  # Shift elements in the sorted part
            if arr[j - 1] > key:
                arr[j] = arr[j - 1]
            else:
                break  # Exit loop if the correct position is found
        arr[j] = key  # Insert key at the correct position
    return arr

# Example Usage
arr = [5, 3, 8, 6, 2]
print(insertion_sort(arr))  # Output: [2, 3, 5, 6, 8]
