# def insert_at_last(arr, element):
#     # n = len(arr) # New size of the array
#     # arr = arr + [None]  # Expanding array without a loop
#     # arr[n] = element  # Assigning the new element at the last position
#     # return arr

#     new_arr = []

    
# arr = [10,20,30,40]
# result = insert_at_last(arr, 50)
# print(result)


def insert_at_last(arr, element):
    arr_new = [None]*(len(arr)+1)
    for i in range(len(arr)):
        arr_new[i] = arr[i]
    arr_new[len(arr)] = element
    return arr_new

arr = [10,20,30,40,90]
result = insert_at_last(arr, 50)
print(result)