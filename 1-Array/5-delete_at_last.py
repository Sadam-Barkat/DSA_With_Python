def delete_at_last(arr):
    if len(arr) == 0:
        return f"arr is empty"
    
    new_arr = [0] * (len(arr) - 1)

    for i in range(len(arr) -1):
        new_arr[i] = arr[i]

    return new_arr

arr = [1,2,3,4,5]    
result  = delete_at_last(arr)
