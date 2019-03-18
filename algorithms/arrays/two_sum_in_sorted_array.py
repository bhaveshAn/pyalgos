def two_sum_sorted_array(arr, n, target):

    i = 0
    j = n - 1

    while i < j:
        if arr[i] + arr[j] < target:
            i += 1
        elif arr[i] + arr[j] > target:
            j -= 1
        else:
            return i+1, j+1

    return None


arr = [1,2,3,4,6,7,8,9]
target = 14
print(two_sum_sorted_array(arr, len(arr), target))
