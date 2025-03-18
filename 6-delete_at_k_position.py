def delete_at_k_position(arr, k):
    if k < 0 or k > len(arr):
        return f"index out of range"
    
    new_arr = [0] * (len(arr) - 1)

    for i in range(len(arr) - 1):
        if i < k:
            new_arr[i] = arr[i]
        else:
            new_arr[i] = arr[i + 1]  
    return new_arr

arr = [1,2,3,4,5]      
position = 2
print("Before delete")
print(arr)
result = delete_at_k_position(arr, position)
print("After delete")
print(result)
