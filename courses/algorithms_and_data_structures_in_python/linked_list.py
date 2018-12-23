class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_start(self, data):
        self.size += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_end(self, data):
        self.size += 1
        new_node = Node(data)
        node = self.head

        while node.next is not None:
            node = node.next

        node.next = new_node

    def remove(self, data):
        self.size -= 1
        node = self.head
        prev = None
        while node.data != data:
            prev = node
            node = node.next

        if prev is None:
            self.head = node.next
        else:
            prev.next = node.next

    def traverse(self):

        node = self.head

        while node is not None:
            print(node.data)
            node = node.next
