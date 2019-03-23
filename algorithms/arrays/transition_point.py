def transition_point(arr, n):
    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == 0:
            l = mid + 1
        elif arr[mid] == 1:
            if arr[mid-1] == 0:
                return mid
        else:
            r = mid - 1
    return -1


arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
n = len(arr)

print(transition_point(arr, n))
