class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if stack and self.isClosing(stack[-1], c):
                stack.pop()
            else:
                stack.append(c)
        
        if len(stack) == 0:
            return True
        return False


    def isClosing(self, a: str, b: str) -> bool:
        if ((a == '[' and b == ']') or
        (a == '(' and b == ')') or
        (a == '{' and b == '}')):
           return True
        return False
        
        