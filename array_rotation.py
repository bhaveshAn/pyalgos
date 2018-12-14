def array_rotation(arr, n):
    for i in range(n):
        array_rotation_by_one(arr)
    return arr

def array_rotation_by_one(arr):
    a = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[-1] = a


