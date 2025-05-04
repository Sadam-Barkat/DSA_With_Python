class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.stack_size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.stack_size += 1

    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
        else:
            self.head = self.head.next
            self.stack_size -= 1

    def top(self):
        if self.is_empty():
            print("Stack is Empty")
        else:
            print("Top Element is:", self.head.data)

    def is_empty(self):
        return self.head is None

    def size(self):
        print("Stack Size is:", self.stack_size)

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Example usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.top()
s.size()
s.pop()
s.display()
