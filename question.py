# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         prevNum = {}
        
#         for i, n in nums:
#             diff = target -n
#             if diff in prevNum:
#                 return [prevNum[diff], i]
#             prevNum[n]= i
        


# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy= ListNode()
#         cur= dummy
#         carry = 0
        
# while l1 or l2 or carry:
#     v1 = l1.val if l1 else 0
#     v2= l2.val if l2 else 0
            
#     val = v1+v2+carry
#     carry = val //10
#     val = val%10
#     cur.next = ListNode(val)
#     cur = cur.next
#     l1 = l1.next if l1 else None
#     l2 = l2.next if l2 else None
# return dummy.next
            
        
# Given a string s, find the length of the longest substring without repeating characters.
# s= 'BAB'
# charSet = set()
# l= 0
# res = 0
# for r in range(len(s)):
#     print(r)
#     while s[r] in charSet:
#         print(s[r])
#         charSet.remove(s[l])
#         l+=1
#     charSet.add(s[r])
#     res = max(res, r-l +1)

from multiprocessing import dummy
import re
from turtle import right


nums = [1,2,3,4]
charSet = set(nums)
print(charSet)
if(len(charSet) != len(nums)):
    print(True)
else:
    print(False)

#OR

# return False if len(set(nums))==len(nums) else True


# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.


    
nums = [4,1,2,1,2]

res = 0
for i in nums:
    res = i ^ res
print(res)



#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
        p1 = 0
        p2 = 0
        sum = arr[0]
        if(sum == s):
            return (1,1)
        if(s == 0):
            return {-1}
        while (p2 < n-1):
            if(sum + arr[p2+1] <= s):
                sum += arr[p2+1]
                p2+=1
                
            else:
                sum -= arr[p1]
                p1+=1
                
            if(sum == s):
                return(p1+1, p2+1)
            
                
        return {-1}

# Given an array of N integers arr[] where each element represents the max length of the jump that can be made forward from that element. Find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then you cannot move through that element.

# class Solution:
	# def minJumps(self, arr, n):
	#     maxR = arr[0]
	#     step = arr[0]
	#     jump=1
	    
	#     if(n==1):
	#         return 0
	#     elif(arr[0] == 0):
	#         return -1
	#     else:
	#         for i in range(n):
	#             i+=1
	#             if(i==n-1):
	#                 return jump
	#             maxR = max(maxR, i+arr[i])
	#             step-=1
	#             if(step==0):
	#                 jump+=1
	#                 if(i>=maxR):
	#                     return -1
	#                 step = maxR-i


# Given a sorted array of size N and an integer K, find the position at which K is present in the array using binary search.


# class Solution:	
# 	def binarysearch(self, arr, n, k):
# 	    low = 0
# 	    high = n-1
# 	    while low<= high:
# 	        mid = low+(high-low)//2
# 	        if(arr[mid] == k):
# 	            return mid
# 	        elif(arr[mid]>k):
# 	            high = mid-1
# 	        else:
# 	            low=mid+1
# 	    return -1           


# Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.

#Function to reverse every sub-array group of size k.
# def reverseInGroups(self, arr, N, K):
# 	i=0
# 	while(i<N):
# 		left = i
# 		right = min(i+K-1, N-1)
# 		while(left< right):
# 		    arr[left], arr[right] = arr[right], arr[left]
# 		    left +=1
# 		    right-=1
# 		i += K

# Given two arrays A and B of equal size N, the task is to find if given arrays are equal or not. Two arrays are said to be equal if both of them contain same set of elements, arrangements (or permutation) of elements may be different though.


def check(self,A,B,N):
    A.sort()
    B.sort()
    for i in range(N):
        if(A[i] != B[i]):
            return False
    return True

# Given an array Arr (distinct elements) of size N. Rearrange the elements of array in zig-zag fashion. The converted array should be in form a < b > c < d > e < f. The relative order of elements is same in the output i.e you have to iterate on the original array only.

arr = [4, 3, 7, 8, 6, 2, 1]
n = 7
flag= True
for i in range(n-1):
    if flag is True:
        if arr[i]> arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    else:
        if arr[i]< arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    flag = bool(1-flag)


# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currSum =0
        for i in nums:
            if currSum <0:
                currSum = 0
            currSum += i
            maxSub = max(maxSub, currSum)
        return maxSub

# Given an array of n integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 


def findmindiff(arr, n, m):
    if m==0 or n == 0:
        return 0
    arr.sort()
    if n <m:
        return -1
    min_diff = arr[n-1] - arr[0]
    
    for i in range(len(arr)-m+1):
        min_diff = min(min_diff, arr[i+m-1]- arr[i])
    return min_diff
    


if __name__ == "__main__":
    arr = [12, 4, 7, 9, 2, 23, 25, 41,
          30, 40, 28, 42, 30, 44, 48,
          43, 50]
    m = 7  # Number of students
    n = len(arr)
    print("Minimum difference is", findmindiff(arr, n, m))
 

#  Given a linked list of N nodes. The task is to reverse this list.


class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
# Given a singly linked list of size N of integers. The task is to check if the given linked list is palindrome or not.
class Solution:
    def isPalindrome(self, head):
        #code here
        nums=[]
        
        while head:
            nums.append(head.data)
            head = head.next
        l = 0
        r = len(nums) - 1
        
        while l<=r:
            if nums[l] != nums[r]:
                return False
            l +=1
            r-=1
        return True
# Remove duplicate element from sorted Linked List

def removeDuplicates(head):
    curr = head
    while curr:
        while curr.next and curr.next.data == curr.data:
            curr.next = curr.next.next
        
        curr = curr.next
    return curr

# Remove duplicates from an unsorted linked list

class Solution:
    def removeDuplicates(self, head):
        # code here
        d = {}
        curr =head
        prev = None
        while curr:
            if curr.data in d:
                prev.next = curr.next
                curr = curr.next
            
            else:
                d[curr.data] = 1
                prev = curr
                curr = curr.next
        return head

# 21. Merge Two Sorted Lists

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val<list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next

# Multiply two numbers represented by Linked Lists

def multiplyTwoLists(first, second):
    num1 = 0
    num = 0
    first_ptr = first.head
    second_ptr = second.head

    while first_ptr != None or second_ptr != None:
        if first_ptr != None:
            num1 = (num1*10)+ first_ptr.data
            first_ptr= first_ptr.next
        elif second_ptr != None:
            num2 = (num2 * 10) + second_ptr.data
            second_ptr = second_ptr.next
    
    return num1*num2

# 19. Remove Nth Node From End of List

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummyNode = ListNode(0, head),
    left = dummyNode
    right = head
    while n>0 and right:
        right = right.next
        n-=1

    while right:
        left = left.next
        right = right.next
    
    left.next = left.next.next
    return dummyNode.next

# 160. Intersection of Two Linked Lists
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1 = headA
        l2 = headB
        while l1!=l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1

# Reverse a Doubly Linked List

def reverseDLL(head):
    #return head after reversing
    curr = head
    if curr == None or curr.next == None:
        return head
    while curr.next:
        curr = curr.next
    head = curr
    curr.next = curr.prev
    curr.prev = None
    curr = curr.next
    while curr.prev != None:
        temp = curr.next
        curr.next = curr.prev
        curr.prev =temp
        curr = curr.next
    curr.prev = curr.next
    curr.next = None
    return head

# Delete nodes having greater value on right

class Solution:
    def reverse(head):
        prev = None
        curr = head
        while curr!=None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        
    def compute(self,head):
        #Your code here
        head = Solution.reverse(head)
        curr = head
        ma = head.data
        prev = head
        head = head.next
        while head !=None:
            if head.data >= ma:
                ma = head.data
                prev= head
                head = head.next
            else:
                prev.next = head.next
                head = prev.next
                
        head = Solution.reverse(curr)
        return head

# Detect Loop in linked list
class Solution:
    def detectLoop(self, head):
        low= head 
        high = head

        while low!=None and high!=None and high.next!=None:
            low = low.next
            high = high.next.next
            if low == high:
                return True
        return False



# Remove loop in Linked List
class Solution:
    def removeLoop(self, head):
        low = head 
        high = head
        while low!= None and high!=None and high.next!= None:
            low = low.next
            high = high.next.next
            if low == high:
                break
        
        if low == head:
            while high.next != low:
                high = high.next
            high.next = None
        elif low == high:
            low = head
            while low.next != high:
                low = low.next
                high = high.next
            high.next = None
            
# Nth node from end of linked list
def getNthFromLast(head,n):
    p = head
    f = head
    cnt = 1
    while cnt<=n-1:
        if f.next != None:
            f = f.next
            cnt +=1
        else:
            return -1
    while f.next!=None:
        p= p.next
        f = f.next
    return p.data

# Rotate a Linked List

def rotate(self, head, k):
    pntr = head
    cnt =1
    while pntr != None:
        if cnt == k:
            break
        pntr = pntr.next
    
    new_head = pntr.next
    if pntr.next:
        pntr.next = None
        q = new_head
        while q.next != None:
            q = q.next
        q.next = head
        return new_head
    else:
        return head


# Add two numbers represented by linked lists
def addTwoLists(self, first, second):
    def reverse(head):
        curr = head
        prev = None
        nxt = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    first = reverse(first)
    second = reverse(second)
    carry = 0
    res = None
    curr = None

    while first!= None or second != None:
        sum = (first.data if first else 0) + (second.data if second else 0) + carry
        carry = sum//10
        digit = sum%10
        temp = Node(digit)
        
        if res == None:
            res =temp
        else:
            curr.next = temp
        curr = temp
        
        if first:
            first = first.next
        if second:
            second = second.next

    if carry != 0:
        temp = Node(carry)
        curr.next = temp
        curr = temp
    res = reverse(res)
    return res


    

# Reverse a Linked List in groups of given size.
def reverse(self,head, k):
        curr= head
        prev = None
        nxt = None
        count = 0

        while curr != None and count < k:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            count +=1
            
        if nxt:
            head.next = Solution().reverse(nxt, k)
        return prev

# Delete without head pointer
def deleteNode(self,curr_node):
    next_node = curr_node.next
    curr_node.data = next_node.data
    curr_node.next = None

# Check If Circular Linked List

def isCircular(head):
    c1 = head
    c2 = head
    while c1 and c2 and c2.next:
        c1 = c1.next
        c2= c2.next.next
        if c1 == c2:
            return 1
    return 0

# Delete Middle of Linked List

def deleteMid(head):
    '''
    head:  head of given linkedList
    return: head of resultant llist
    '''
    curr = head
    count = 1
    
    
    while curr.next:
        curr = curr.next
        count+=1
    
    if curr == head or curr == None:
        return None
        
    curr = head
    c= 0

    while c< count//2:
        prev = curr
        curr = curr.next
        c +=1
    
    prev.next = curr.next
    
    return head
        
