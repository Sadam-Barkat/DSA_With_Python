def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]    

    return arr

my_arr = [2,1,4,6,9,0]      
print("Before sorting")
print(my_arr)  

result = selection_sort(my_arr)
print("After sorting")
print(result)