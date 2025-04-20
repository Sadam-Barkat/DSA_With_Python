def partition(arr, left, right):
    pivot = arr[left]
    P = left + 1
    Q = right

    while True:
        while P <= Q and arr[P] <= pivot:
            P += 1
        while P <= Q and arr[Q] > pivot:
            Q -= 1
        if P <= Q:
            arr[P], arr[Q] = arr[Q], arr[P]
        else:
            break

    arr[left], arr[Q] = arr[Q], arr[left]
    return Q

def quick_sort(arr, left, right):
    if left < right:
        pi = partition(arr, left, right)
        quick_sort(arr, left, pi - 1)
        quick_sort(arr, pi + 1, right)

# Driver code
arr = [4, 3, 5, 2, 6, 1]
print("Array Before Sorting:", arr)

quick_sort(arr, 0, len(arr) - 1)

print("Array After Sorting:", arr)
