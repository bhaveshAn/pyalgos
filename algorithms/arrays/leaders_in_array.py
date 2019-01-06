'''
Leaders in an array
'''

def leaders_in_array(arr, n):

	max_ = arr[-1]
	print(max_)

	for i in range(n-2, -1, -1):

		if max_ < arr[i]:
			print(max_)
			max_ = arr[i]