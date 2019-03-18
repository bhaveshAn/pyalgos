def greater_on_right_side(arr, n):

    max_ = arr[n-1]

    arr[n-1] = -1

    for i in range(n-2, -1, -1):
        tmp = arr[i]
        arr[i] = max_
        if max_ < tmp:
            max_ = tmp

    return arr

arr = [3,4,5,6,7,8,9,8,7,6,5,4]
n = len(arr)
arr = greater_on_right_side(arr, n)

for i in arr:
    print(i, end=' ')
print()
