#1D Array

# print('How many elements to store inside an array', end=" ")
# num= input()
# arr = []
# print('\nEnter', num, 'Element:', end= '' )
# num = int(num)
# for i in range (num):
#     element = input()
#     arr.append(element)
# print('\n The array elements are: ')
# for element in arr:
#     print(element, end= '')


#2D array

r_num= int(input('Enter number of rows'))
c_num = int(input('Enter number of columns'))
twod_arr= [[5 for col in range(c_num)] for row in range(r_num)]

for row in range(r_num):
    for col in range(c_num):
        twod_arr[row][col] = row*col
print(twod_arr)