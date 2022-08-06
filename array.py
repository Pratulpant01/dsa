# 1D Array

print('How many elements to store inside an array', end=" ")
num= input()
arr = []
print('\nEnter', num, 'Element:', end= '' )
num = int(num)
for i in range (num):
    element = input()
    arr.append(element)
print('\n The array elements are: ')
for element in arr:
    print(element, end= '')


# 2D array

r_num= int(input('Enter number of rows'))
c_num = int(input('Enter number of columns'))
twod_arr= [[5 for col in range(c_num)] for row in range(r_num)]

for row in range(r_num):
    for col in range(c_num):
        twod_arr[row][col] = row*col
print(twod_arr)


#Implement searching inside an array

#Delete element inside an array

print('Enter the size of an array')

tot = int(input())
arr = []

print('Enter elements in your array2:') 


for i in range(tot):

    arr.append(input())
print('Enter the value to delete:') 

val = input()

if val in arr:
    arr.remove(val)
    print('The new array is:')
    for i in range(tot-1):
        print(arr[i])
else:
    print('Element doesnt exist')

# Sort array in python

from operator import le


arr = [12,102, 25, 45, 32, 67, 89]
temp = 0

print("Elements of an original array is:")

for i in range(len(arr)):
    print(arr[i])
#Sorting

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i]> arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print()

print('Elements sorted in ascending order are:')
for i in range(len(arr)):
    print(arr[i])


# Search and see elements in an array

import array

arr = array.array('i', [1,3,4,5,4,3,2,3,2,4,5,4,5,5])

print('The newely created array is:')

for i in range(len(arr)):
    print(arr[i])

print('The index of first occurence of 2 is')
print(arr.index(2))


#array python