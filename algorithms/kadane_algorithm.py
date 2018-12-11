# Largest Sum Contiguous Subarray

try:
    from sys import maxint # Python 2
except ImportError:
    from sys import maxsize as maxint # Python 3


def kadane(arr):
    max_so_far = -maxint - 1
    max_ending_here = 0

    for i in range(len(arr)):
        max_ending_here += arr[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far
    
