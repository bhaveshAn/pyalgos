'''
Implement Two stacks in an array
'''


class TwoStack:

	def __init__(self, n):
		
		self.size = n
		self.array = [0] * n
		self.top1 = 0
		self.top2 = self.size

	def push1(self, data):

		if self.top1 < self.top2:
			self.top1 += 1
			self.array[self.top] = data

		else:
			print('Stack Overflow')
			exit(1)

	def push2(self, data):

		if self.top1 < self.top2:
			self.top2 -= 1
			self.array[self.top2] = data
		else:
			print('Stack Overflow')
			exit(1)

	def pop1(self):

		if self.top1 >= 0:
			x = self.array[self.top1]
			self.top1 -= 1
			return x
		else:
			print('Stack Underflow')
			exit(1)

	def pop2(self):

		if self.top2 < self.size:
			x = self.array[self.top2]
			self.top2 += 1
			return x
		else:
			print('Stack Underflow')
			exit(1)
