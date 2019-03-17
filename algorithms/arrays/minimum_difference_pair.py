import sys


def minimum_difference_pair(arr, n):
    diff = sys.maxsize
    arr = sorted(arr)

    for i in range(n-1):
        if arr[i+1] - arr[i] < diff:
            diff = arr[i+1] - arr[i]

    return diff

arr = [1, 5, 3, 19, 18, 25]
n = len(arr)

print(minimum_difference_pair(arr, n))
