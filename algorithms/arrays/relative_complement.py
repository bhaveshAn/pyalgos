'''
Relative Complement of two sorted arrays
'''

def relative_complement(arr1, arr2):
	i = 0
	j = 0
	n = len(arr1)
	while i < n and j < n:
		if arr1[i] < arr2[j]:
			print(arr1[i], end=' ')
			i += 1
		elif arr1[i] > arr2[j]:
			j += 1
		else:
			i += 1
			j += 1
	print()
    
