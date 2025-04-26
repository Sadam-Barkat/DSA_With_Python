class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def display(node1):
    head = node1
    while head is not None:
        print(head.data)
        head = head.next     

# Create nodes
node1 = Node(10)  
node2 = Node(20)
node3 = Node(30)   
node4 = Node(40)   
node5 = Node(50)

# Linked nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Print linkedlist
display(node1)
