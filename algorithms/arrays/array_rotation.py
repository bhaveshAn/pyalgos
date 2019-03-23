def rotate(arr, n, d):
    temp = [0] * d
    j = 0
    for i in range(d):
        temp[i] = arr[i]

    while j < n - d:
        arr[j] = arr[j+d]
        j += 1
    
    i = 0
    while i < d:
        arr[j] = temp[i]
        j += 1
        i += 1
    return arr
