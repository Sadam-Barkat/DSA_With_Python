def insert_at_k_position(arr, k, elemenet):
    if k < 0 or k > my_len(arr):
        return f"Invalid Position"
    
    new_arr = [0] * (my_len(arr) + 1)

    for i in range(my_len(arr)+1):
        if i < k:
            new_arr[i] = arr[i]
        elif i == k:
            new_arr[i] = elemenet
        else:
            new_arr[i] = arr[i - 1]  
    return new_arr        

if __name__ == "__main__":
    len_of_arr = int(input("Enter the len of arr : "))
    arr = []
    for i in range(len_of_arr):
        value = int(input(f"Enther the arr element-{i+1} : "))
        arr.append(value)

    print("Old ArraY")
    print(arr) 

    element = int(input("Enter the element : "))
    position = int(input("Enter the postion : "))
    new_arr = insert_at_k_position(arr, position, element)
    print("New Array")
    print(new_arr)
