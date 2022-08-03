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



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def traversal(self1):
        if self1.head is None:
            print('Singly Linked List is empty')
        else:
            a = self1.head  # Creating a temp variable to assign self.head so that it is not changed
            while a is not None:
                print(a.data, end= "=>")
                a = a.next
    # Insert data at beginning
    def add_at_begin(self2, data):
        print()
        nb = Node(data)
        nb.next = self2.head
        self2.head = nb

    #Insert data at end

    def insert_at_end(self3, data):
        print()
        ne = Node(data)
        a= self3.head
        while a.next is not None:
            a = a.next
        a.next = ne

    # Insert in between

    def insert_in_between(self4, position, data):
        print()
        nb= Node(data)
        a=self4.head

        for i in range(1, position-1):
            a=a.next
        
        nb.next = a.next
        a.next = nb
        
    # Deletion in beginning
    def delete_in_begin(self):
        print()
        a= self.head
        self.head = a.next
        a.next = None

    #Deletion at end

    def delete_at_end(self):
        print()
        previous = self.head
        a= self.head.next
        while a.next is not None:
            a= a.next
            previous = previous.next
        previous.next = None

    # Deletion in between

    def delete_in_between(self, position):
        print()

        previous = self.head
        a= self.head.next

        for i in range(1, position-1):
            a= a.next
            previous = previous.next
        
        previous.next = a.next
        a.next = None


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
sll.insert_in_between(3, 40)
sll.traversal()
sll.delete_in_between(3)
sll.traversal()

#Linked List 
