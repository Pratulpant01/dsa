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


           