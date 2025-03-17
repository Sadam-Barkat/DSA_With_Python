def delete_at_first(arr):
    if len(arr) == 0:
        return f"Empty Array"
    
    new_arr = [0] * (len(arr) - 1)
    
    for i in range(1, len(arr)):
        new_arr[i - 1] = arr[i]
    return new_arr    

if __name__== "__main__":
    len_arr = int(input("Enter the len of arr : "))
    arr = []
    for i in range(len_arr):
        element = int(input(f"Enter the element-{i+1} : "))
        arr.append(element)
    print("Before delete") 
    print(arr)   
    result = delete_at_first(arr) 
    print("After delete")
    print(result)   