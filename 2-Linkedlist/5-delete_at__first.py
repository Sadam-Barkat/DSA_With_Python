class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_at_first(node):
    head = node
    head = head.next
    return head

def display(node):
    head = node
    while head is not None:
        print(head.data)
        head = head.next

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

display(delete_at_first(node1))


