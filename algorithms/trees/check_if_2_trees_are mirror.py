class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


def is_mirror(node1, node2):

    if not node1 and not node2:
        return True

    elif not node1 or not node2:
        return False

    return node1.data == node2.data and is_mirror(node1.left, node2.right) and is_mirror(node1.right, node2.left)


root1 = Node(1) 
root2 = Node(1) 
  
root1.left = Node(2) 
root1.right = Node(3) 
root1.left.left = Node(4) 
root1.left.right = Node(5) 
  
root2.left = Node(3) 
root2.right = Node(2) 
root2.right.left = Node(5) 
root2.right.right = Node(4) 
  
if is_mirror(root1, root2): 
    print ("Yes") 
else: 
    print ("No") 
