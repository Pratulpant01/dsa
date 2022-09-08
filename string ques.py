# Reverse a String

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
