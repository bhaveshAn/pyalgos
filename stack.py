class Stack:

    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if self.isEmpty():
            raise Exception("nothing to pop")
        return self.stack.pop(len(self.stack)-1)

    def peek(self):
        if self.isEmpty():
            raise Exception("Nothing to peek")
        return self.stack[len(self.stack)-1]

    def __sizeOf__(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0

