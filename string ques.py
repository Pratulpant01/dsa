# Reverse a String

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
            
