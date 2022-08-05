from logging import root
from tkinter.messagebox import NO


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
    def traPreOrder(self):
        print(self.val, end= '=>')
        if self.left:
            self.left.traPreOrder()
        if self.right:
            self.right.traPreOrder()
        
    def traInOrder(self):
        if self.left:
            self.left.traInOrder()
        print(self.val, end= '=>')
        if self.right:
            self.right.traInOrder()
    
    def traPostOrder(self):
        if self.left:
            self.left.traPostOrder()
        if self.right:
            self.right.traPostOrder()
        print(self.val, end= '=>')

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(9)

print('\n InOrder Traversal')
root.traInOrder()
print('\n PostOrder Traversal')

root.traPostOrder()
print('\n PreOrder Traversal')

root.traPreOrder()