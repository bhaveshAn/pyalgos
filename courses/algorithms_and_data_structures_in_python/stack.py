class Stack:

	def __init__(self):
		self.stack = []

	def push(self, data):
		self.stack.append(data)

	def pop(self):
		data = self.stack[-1]
		del self.stack[-1]
		return data

	def size(self):
		return len(self.stack)

	def is_empty(self):
		return self.stack == []

	def peek(self):
		return self.stack[-1]