def union(arr1, arr2, m, n):

    arr1 = sorted(arr1) # If not sorted
    arr2 = sorted(arr2) # If not sorted

    i = j = 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            print(arr1[i], end=' ')
            i += 1
        elif arr1[i] > arr2[j]:
            print(arr2[j], end=' ')
            j += 1
        else:
            print(arr1[i], end=' ')
            i += 1
            j += 1

    while i < m:
        print(arr1[i], end=' ')
        i += 1

    while j < n:
        print(arr2[j], end=' ')
        j += 1


def intersection(arr1, arr2, m, n):
    arr1 = sorted(arr1) # If not sorted
    arr2 = sorted(arr2) # If not sorted

    i = j = 0
    while i < m and j < n:
       if arr1[i] < arr2[j]:
            i += 1
       elif arr1[i] > arr2[j]:
            j += 1
       else:
            print(arr1[i], end=' ')
            i += 1
            j += 1



arr1 = [1,2,3,4,6,7,8,9]
arr2 = [3,4,5,6,7,8,9]

print("Union of arrays : ")
union(arr1, arr2, len(arr1), len(arr2))
print()

print("Intersection of arrays : ")
intersection(arr1, arr2, len(arr1), len(arr2))
print()
