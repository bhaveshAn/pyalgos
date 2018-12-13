def bitwise_and(n, k):
    return(k-1 if (k-1)|k <= n else k-2)
