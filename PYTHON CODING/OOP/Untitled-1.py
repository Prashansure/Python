class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printlinkedlist(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

printlinkedlist(head)