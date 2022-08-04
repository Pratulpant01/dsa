from termios import NL1


class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # traverse forward using double linked list

    def forward_traversal(self):
        if self.head is None:
            print("Doubly linked list is empty")
        else:
            a=self.head
            while a is not None:
                print(a.data, end= "<=>")
                a=a.next
                
    # traverse backward using double linked list

    def backward_traversal(self):
        print()
        if self.head is None:
            print("Doubly linked list is empty")
        else:
            a=self.head
            while a.next is not None:
                a= a.next
            while a is not None:
                print(a.data, end= "<=>")
                a=a.previous
n1 = Node(5)
dll = DoublyLinkedList()
dll.head = n1
n2 = Node(4)
n1.next = n2
n1.previous = None
n3 = Node(6)
n2.next = n3
n2.previous = n1
n4= Node(8)
n3.next = n4
n3.previous = n2
n5 = Node(19)
n4.next = n5
n4.previous= n3

n5.previous = n4
n5.next = None

dll.forward_traversal()
dll.backward_traversal()

            
        