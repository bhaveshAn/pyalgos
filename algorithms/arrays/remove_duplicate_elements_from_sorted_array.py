def remove_duplicates(arr, n):
    j = 0
 
    for i in range(0, n-1):
        if arr[i] != arr[i+1]:
            arr[j] = arr[i]
            j += 1
    arr[j] = arr[n-1]
    j += 1
    return arr
