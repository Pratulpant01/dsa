# Reverse a String

from itertools import count
from operator import le


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
