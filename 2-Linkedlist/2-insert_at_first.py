class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_first(val, node1):
    head = node1
    new_node = Node(val)
    new_node.next = head
    head = new_node
    return head

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

print("Before Insetion")
display(node1)

node = insert_at_first(60, node1)
print("After Insertion")
display(node)


