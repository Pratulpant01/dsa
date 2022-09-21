# Reverse a String

from collections import deque
from itertools import count
from operator import le
import re


def reverseWord(s):
    #your code here
    s1 = ''
    for i in s:
        s1 = i+s1
    return s1
    
# Parenthesis Checker

def ispar(self,x):

    def isOpening(c):
        return (c == '(') or (c == '[') or (c == '{')
    
    def isClosing(a, b):
        return (a == '(' and b == ')') or (a== '{' and b == '}') or (a == '[' and b == ']')
    
    s = []

    for i in x:
        if isOpening(i):
            s.append(i)
        else:
            if not s:
                return False
            elif not isClosing(s[-1], i):
                return False
            else:
                s.pop()
    return True if not s else False
            

# Reverse words in a given string

def reverseWords(self,S):
    a = S.split()
    left = 0
    right = len(S)-1

    while left< right:
        a[left], a[right] = a[right], a[left]
        left+=1
        right-=1
    
    return ".".join(a)


# Implement strstr

def strstr(s,x):
    if s == '':
        return 0
    
    for i in range(len(s)+1 - len(x)):
        if s[i: i+len(x)] == x:
            return i
    return -1

# Anagram

def isAnagram(self,a,b):
    if len(a) != len(b):
        return False

    countA = {}
    countB = {}

    for i in range(len(a)):
        countA[a[i]] = 1 + countA.get(a[i], 0)
        countB[b[i]] = 1 + countB.get(b[i], 0)

    for c in countA:
        if countA[c] != countB.get(c, 0):
            return False
    return True


# Check if string is rotated by two places

def isRotated(self, str1, str2):

    if str1 != str2:
        return False
    if len(str1)<2:
        return str1 == str2
    
    clock_rot = ''
    anti_rot = ''
    l = len(str2)

    anti_rot = (anti_rot + str2[l-2:] + str2[0:l-2])
    clock_rot = (clock_rot + str2[2:] + str2[0:2])

    return (str1 == anti_rot) or (str1 == clock_rot)




# Longest Common Prefix in an Array

def longestCommonPrefix(self, arr, n):

    res = ''

    for i in range(len(arr[0])):
        for s in arr:
            if i == len(s) or s[i] != arr[0][i]:
                if res == '':
                    return -1
                return res
        res += arr[0][i]

    return res

# Reverse a string using Stack

def reverse(S):
    stack = []
    res = ''

    for i in S:
        stack.append(a)
    
    for i in S:
        res = res + stack.pop()
    return res

# Anagram of String

def remAnagram(str1,str2):
    S1 = len(str1)
    S2 = len(str2)
    str1 = list(str1)
    str2 = list(str2)
    dup = 0
    if S1 > S2:
        for i in str2:
            if i in str1:
                dup += 1
                str1.remove(i)
    else:
        for i in str1:
            if i in str2:
                dup += 1
                str2.remove(i)
    return (S1 - dup) + (S2 - dup) 

# Remove Duplicates
def removeDups(self, S):
    l = []

    for i in S:
        if i not in l:
            l.append(i)
    return ''.join(l)


# Valid Substring
def findMaxLen(ob, S):
        stack = []
        stack.append(-1)
        res = 0
        
        for i in range(len(S)):
            if S[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    res = max(res, i - stack[-1])
                else:
                    stack.append(i)
                    
        return res

# Check if strings are rotations of each other or not

def areRotations(self,s1,s2):
        #code here
        
        temp = s1 + s1
        if len(s1)!= len(s2):
            return 0
        
        if s2 in temp:
            return 1
        else:
            return 0

# Kadane's Algorithm
# if the sum of a sub array is negative set 
# the complete sum to 0 and start calculating sum again 

def maxSubArraySum(self,arr,N):
    currSum= 0
    maxSum = arr[0]

    for i in range(len(arr)):
        currSum = currSum + arr[i]

        if currSum> maxSum:
            maxSum = currSum
        if currSum<0:
            currSum = 0
    
    return maxSum

# Majority Element

def majorityElement(self, A, N):
    res = 0
    count = 0

    for n in A:
        if count == 0:
            res = n
        count += 1 if n == res else -1
    
    count = 0
    for i in a:
        if res == i:
            count+=1
    
    if count<= (N//2):
        return -1
    else:
        return res



# Count Inversions

def inversionCount(self, arr, n):
        temp_arr = [0] * n
        
        return Solution().mergeSort(arr, temp_arr, 0, n-1)
        
    # def mergeSort(self, arr, temp_arr, left, right):
  
        inv_count = 0
        if left < right:
  
            mid = (left + right)//2
  
  
            inv_count += Solution().mergeSort(arr, temp_arr,
                                left, mid)
  
  
            inv_count += Solution().mergeSort(arr, temp_arr,
                                mid + 1, right)
  
  
            inv_count += Solution().merge(arr, temp_arr, left, mid, right)
        return inv_count
  
    # def merge(self, arr, temp_arr, left, mid, right):
        i = left     
        j = mid + 1 
        k = left    
        inv_count = 0
  

  
        while i <= mid and j <= right:
  

            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                k += 1
                i += 1
            else:
                temp_arr[k] = arr[j]
                inv_count += (mid-i + 1)
                k += 1
                j += 1

        while i <= mid:
            temp_arr[k] = arr[i]
            k += 1
            i += 1

        while j <= right:
            temp_arr[k] = arr[j]
            k += 1
            j += 1
  
        for loop_var in range(left, right + 1):
            arr[loop_var] = temp_arr[loop_var]
  
        return inv_count
            
# Maximum Occuring Character

def getMaxOccurringChar(self,s):
    max = -1
    res = {}
    result = ''

    for i in s:
        res[s[i]] = 1+ res.get(i, 0)
    
    for i in range(len(s)):
        if max< res[s[i]]:
            max = res[s[i]]
            result = s[i]
    
    return result
        

# Maximum Product Subarray

def maxProduct(self,arr, n):

    res = max(arr)
    currMax, currMin = 1,1

    for i in arr:
        if i ==0:
            currMax, currMin = 1,1
        
        temp = currMax*i
        currMax = max(currMax*i, currMin*i, i)
        currMin = min(currMin*i, temp, i)

        res = max(res, currMax)

    return res

# Find Missing And Repeating

def findTwoElement( self,arr, n):
    result = [0,1]

    for i in range(len(arr)):
        if arr[abs(arr[i])-1]<0:
            result[0] = abs(arr[i])
        else:
            arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]

    for i in range(len(arr)):
        if arr[i]>0:
            result[1] = arr[i]
            break
    return result
        

# Maximum of all subarrays of size k

def max_of_subarrays(self,arr,n,k):
    q = deque()
    res = []

    for i in range(k):
        while q and arr[i] >= arr[q[-1]]:
            q.pop()
        q.append(arr[i])

    for i in range(k, n):
        res.append(arr[q[0]])

        while q and q[0] <= i-k:
            q.popleft()
        
        while q and arr[i]>= arr[q[-1]]:
            q.pop()
        q.append(arr[i])

    res.append(arr[q[0]])
    return res

# K-th element of two sorted Arrays

def kthElement(self,  arr1, arr2, n, m, k):
    res = []
    i=0
    j=0
    d=0

    while i<n and j<m:
        if arr1[i]< arr2[j]:
            res.append(arr1[i])
            i+=1
        else:
            res.append(arr2[j])
            j+=1
        d+=1
    
    while i<n:
        res.append(arr1[i])
        i+=1
        d+=1

    while j<n:
        res.append(arr2[j])
        j+=1
        d+=1
    
    return res[k-1]

# Missing number in array

def MissingNumber(self,array,n):
    expectedSum = (n*(n+1))//2

    total = 0

    for i in array:
        total +=1
    
    return expectedSum - total

# Smallest Positive missing number

def missingNumber(self,arr,n):
    for i in range(len(arr)):
        if arr[i] <0:
            arr[i] = 0
    
    for i in range(n):
        val = abs(arr[i])
        
        if 1<= val <= n:
            if arr[val-1]> 0:
                arr[val-1] *= -1
            if arr[val-1] == 0:
                arr[val-1] = -1 * (n+1)
    
    for i in range(1, n+1):
        if arr[i-1]>= 0:
            return i
    
    return n+1

        

# Minimum Swaps to Sort

def minSwaps(self, nums):
    swap =0
    a = sorted(nums)
    res = {}
    n = len(nums)
    temp = 0

    for i in range(n):
        res[nums[i]] = i
    

    for i in range(n):
        if nums[i] != a[i]:
            swap +=1
            temp = nums[i]

            nums[i], nums[res[a[i]]] = nums[res[a[i]]], nums[i]
            res[temp] = res[a[i]]
            res[a[i]] = i
    return swap

# Sort an array of 0s, 1s and 2s Part 1


def sort012(self,arr,n):
        # code here
        a = 0
        b = 0
        c = 0
        
        for i in arr:
            if i == 0:
                a +=1
            elif i ==1:
                b+=1
            else:
                c+=1
        
        for i in range(a):
            arr[i] = 0
        for i in range(a, b):
            arr[i] = 1
        for i in range(a+b, a+b+c):
            arr[i] = 2
        
        return arr

# Insert in a Sorted List

def sortedInsert(self, head1,key):
        curr = head1
        temp = Node(key)

        while curr and curr.data < key:
            prev = curr
            curr = curr.next
    
        if curr == head1:
            temp.next = head1
            head1 = temp
    
        else:
            nxt = prev.next
            prev.next = temp
            temp.next = nxt
    
        return head1


# Rotate Array

def rotateArr(self,A,D,N):
    def rotate(arr, low, high):
        while low<high:
            arr[low], arr[high] = arr[high], arr[low]
            low+=1
            high-=1
        

    D = D%N

    reverse(A,0, D-1)
    reverse(A, D, N-1)
    reverse(A, 0, N-1)

    return A

# Find duplicates in an array

def duplicates(self, arr, n): 
    result = [0] * n
    ans = []
    for i in range(n):
        result[arr[i]] +=1
    
    for i in range(len(result)):
        if result[i] >1:
            ans.append(i)
        
    if not ans:
        ans.append(-1)
            
    return ans

        
# Remove duplicate elements from sorted Array

def remove_duplicate(self, A, N):
    j = 0
    for i in range(N):
        if A[i] != A[i+1]:
            A[j] = A[i]
            j+=1
    A[j] = A[N-1]
    j+=1

    return j


# Sort an array of 0s, 1s and 2s
def sort012(self,arr,n):

    l = 0
    m=0
    h = n-1

    while m<=h:
        if arr[m] == 0:
            arr[l], arr[m]= arr[m], arr[l]
            l+=1
            m+=1
        elif arr[m] == 2:
            arr[m], arr[h] = arr[h], arr[m]
            h-=1
        elif arr[m] == 1:
            m+=1
    
    return arr

# Largest subarray with 0 sum
def maxLen(self, n, arr):
    maxi = 0
    sum = 0
    res = {}

    for i in range(n):
        sum+=arr[i]
        if sum == 0:
            maxi = i+1
        else:
            if res.get(sum) != None:
                maxi = max(maxi, i-res.get(sum))
            else:
                res[sum] = i
    return maxi

# Intersection of two arrays
def NumberofElementsInIntersection(self,a, b, n, m):

    a.sort()
    b.sort()
    i = 0
    j = 0
    s = set()

    while i<n and j<m:
        if a[i]>b[j]:
            j+=1
        elif a[i]<b[j]:
            i+=1
        else:
            s.add(a[i])
            i+=1
            j+=1
    return len(s)

# Triplet Sum in Array
def find3Numbers(self,A, n, X):
    A.sort()

    for i in range(0, n):
        l= i+1
        r = n-1
        while l<r:
            if A[i] + A[l] + A[r] == X:
                return True
            elif A[i] + A[l] + A[r] <X:
                l+=1
            else:
                r-=1
    return False

# Equilibrium Point
def equilibriumPoint(self,A, N):
    leftSum = 0
    rightSum = 0

    for i in range(N):
        rightSum+= A[i]
    for i in range(N):
        rightSum -= A[i]
        if rightSum == leftSum:
            return i+1
        else:
            leftSum+= A[i]
    return -1

# Smallest Positive missing number

def missingNumber(self,arr,n):
    for i in range(n):
        if arr[i]<0:
            arr[i] = 0
    
    for i in range(n):
        val = arr[i]
        if 1<= val <=n:
            if arr[val-1] >0:
                arr[val-1] *= -1
            elif arr[val-1] == 0:
                arr[val-1] *= -1 (n+1)
    
    for i in range(1, n+1):
        if arr[i-1]>= 0:
            return i
    return n+1


# Peak element
def peakElement(self,arr, n):
    if n == 1:
        return 0
    if arr[0]>= arr[1]:
        return 0
    if arr[n-1]>= arr[n-2]:
        return n-1
    
    for i in range(1, n-1):
        if arr[i]>= arr[i-1] and arr[i]>= arr[i+1]:
            return i

# Union of Two Sorted Arrays
def mergeArrays(self,a,b,n,m):

    i = 0
    j= 0
    res = set()

    while i<n and j<m:
        if a[i]<b[j]:
            res.add(a[i])
            i+=1

        elif a[i]> b[j]:
            res.add(b[j])
            j+=1
        else:
            res.add(a[i])
            i+=1
            j+=1
    while i<n:
        res.add(a[i])
        i+=1
    while j<m:
        res.add(b[j])
        j+=1

    return sorted(res)

