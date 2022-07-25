import array

arr = array.array('i', [1,2,3])

print('The new created array is:', end=' ')

for j in range(0,3):
    print(arr[j], end= ' ')

arr.append(4)

print('The appended array is:', end=' ')

for i in range(0,4):
    print(arr[i], end= ' ')


#Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

        

