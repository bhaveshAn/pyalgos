def missing_num(arr):
    
    n = len(arr)
    total_sum = (n+1) * (n+2) // 2
    sum = 0

    for i in arr:
        sum += i

    return total_sum - sum

