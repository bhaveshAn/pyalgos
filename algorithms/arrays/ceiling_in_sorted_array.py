def ceiling_sorted_array(arr, n, x):
    l = 0
    r = n - 1

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            return arr[mid]
        elif arr[mid] < x:
            if arr[mid + 1] > x:
                return arr[mid+1]
            else:
                l = mid + 1
        else:
            r = mid - 1
    return

arr = [1,2,3,4,5,6,7,9,10,11,14]
n = len(arr)
x = 9
print(ceiling_sorted_array(arr, n, x))
