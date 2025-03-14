def insert_at_first(arr, element):
    # Shift all elements one position to the right
    n = len(arr)
    arr.append(0)  # Increase the size by 1
    for i in range(n, 0, -1):  # Shift elements to the right
        arr[i] = arr[i - 1]
    arr[0] = element  # Insert the new element at index 0

# Example usage:
arr = [10, 20, 30, 40]
insert_at_first(arr, 5)
print(arr)  # Output: [5, 10, 20, 30, 40]
