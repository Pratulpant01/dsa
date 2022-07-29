# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# n1 = Node(5)
# print(n1.data)
# print(n1.next)
        
# #creating a linked list
# class LinkedList:
#     def __init__(self):
#         self.head = None

# sll = LinkedList()

#Traversal in LinkedList

from time import sleep


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def traversal(self):
        if self.head is None:
            print('Singly Linked List is empty')
        else:
            a = self.head  # Creating a temp variable to assign self.head so that it is not changed
            while a is not None:
                print(a.data, end= "=>")
                a = a.next

n1= Node(4)
sll = LinkedList()
sll.head = n1
n2 = Node(5)
n1.next = n2
n3 = Node(10)
n2.next = n3
n4 = Node(12)
n3.next = n4

sll.traversal()

#Linked List 
print(n3.next)
print()