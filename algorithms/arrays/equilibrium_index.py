'''
Equilibrium Index of an array
'''

def equilibrium(arr, n):

	left_sum = 0
	right_sum = 0

	for i in arr:
		right_sum += i

	for i in range(n):

		right_sum -= arr[i]

		if left_sum == right_sum:
			return i

		left_sum += arr[i]

	return None

arr = [-7, 1, 5, 2, -4, 3, 0]

print(equilibrium(arr, len(arr)))