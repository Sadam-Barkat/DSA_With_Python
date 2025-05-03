class Stack:
    def __init__(self):
        self.arr = []
        self.top = -1

    def push(self, a):
        self.top += 1
        self.arr.append(a)

    def pop(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            self.arr.pop()
            self.top -= 1

    def top_element(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print(f"Top Element is: {self.arr[self.top]}")

    def is_empty(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Stack is not empty")

    def display(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            for i in range(self.top + 1):
                print(self.arr[i])

# Driver code
s1 = Stack()
s2 = Stack()

s1.push(10)
s1.push(20)
s1.push(30)
s1.display()
s1.top_element()
s1.pop()
s1.display()
s1.top_element()
s1.push(100)
s1.display()
s1.top_element()
