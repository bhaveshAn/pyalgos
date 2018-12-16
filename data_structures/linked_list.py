class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class List:
    def __init__(self, value):
        self.head = Node(value)

    def insert(self, value):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value)

    def find(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            else:
                current = current.next
        return False

    def delete(self, value):
        if self.find(value) is not True:
            return &quot;Not in list&quot;
        else:
            current = self.head
            while current is not None:
                if current.next.value == value:
                    current.next = current.next.next
                    break
                else:
                    current = current.next

    def print(self):
        current = self.head
        while current is not None:
            if current.value is not None:
                print(current.value)
            current = current.next
