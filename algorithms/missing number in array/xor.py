def missing_num(arr):

    x1 = arr[0]
    x2 = 1

    for i in range(1, len(arr)):
        x1 ^= arr[i]

    for i in range(2, len(arr)+2):
        x2 ^= i

    return x2 ^ x1
