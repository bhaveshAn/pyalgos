class Node:

	def __init__(self, data):
		self.data = data
		self.left  = None
		self.right = None


class BST:

	def __init__(self):
		self.root = None

	def insert(self, data):
		if not self.root:
			self.root = Node(data)
		else:
			self.insert_node(data, self.root)

	def insert_node(self, data, node):
		if data < node.data:
			if node.left:
				self.insert_node(data, node.left)
			else:
				node.left = Node(data)
		else:
			if node.right:
				self.insert_node(data, node.right)
			else:
				node.right = Node(data)

	def min(self):
		if self.root:
			return self.get_min(self.root)

	def get_min(self, node):
		if node.left:
			return self.get_min(node.left)
		else:
			return node.data

	def max(self):
		if self.root:
			return self.get_max(self.root)

	def get_max(self, node):
		if node.right:
			return self.get_max(node.right)
		return node.data

	def traverse(self):
		if self.root:
			self.traverse_in_order(self.root)

	def traverse_in_order(self, node):

		if node.left:
			self.traverse_in_order(node.left)

		print(node.data)

		if node.right:
			self.traverse_in_order(node.right)

	def remove(self, data):
		if self.root:
			self.remove_node(data, self.root)

	def remove_node(self, data, node):
		if data < node.data:
			node.left = self.remove_node(data, node.left)
		elif data > node.data:
			node.right = self.remove_node(data, node.right)
		else:
			if not node.left and not node.right:
				# Leaf Node
				del node
				return None

			if not node.left:
				temp = node.right
				del node
				return temp

			elif not node.right:
				temp = node.left
				del node
				return temp
			temp = self.get_predecessor(node.left)
			node.data = temp.data
			node.left = self.remove_node(temp.data, node.left)

		return node

	def get_predecessor(self, node):
		if node.right:
			return self.get_predecessor(node.right)

		return node

bst = BST()
bst.insert(50)
bst.insert(20)
bst.insert(10)
bst.insert(40)

bst.traverse()