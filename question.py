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
 