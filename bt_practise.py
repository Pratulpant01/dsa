class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    def traPreOrder(self):
        print(self.val, end='=>')
        if self.left:
            self.left.traPreOrder()
        if self.right:
            self.right.traPreOrder()
    
    def traPostOrder(self):
        if self.left:
            self.left.traPostOrder()
        if self.right:
            self.right.traPostOrder()
        print(self.val, end="=>")
    def traInOrder(self):
        if self.left:
            self.left.traInOrder()
        print(self.val, end='=>')
        if self.right:
            self.right.traInOrder()
root = Node(24)
root.left = Node(15)
root.right= Node(10)
root.left.left = Node(19)
root.right.right = Node(21)
root.right.right.left = Node(17)

print('PostOrder')
root.traPostOrder()
print('InOrder')
root.traInOrder()
print('PreOrder')

root.traPreOrder()


# 104. Maximum Depth of Binary Tree

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        