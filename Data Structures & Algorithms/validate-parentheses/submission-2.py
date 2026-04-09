class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if ((c == ']') or
                (c == ')') or
                (c == '}')):
                if stack and ((c == ']' and stack[-1] == '[') or (c == ')' and stack[-1] == '(') or (c == '}' and stack[-1] == '{')):
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(c)
            
        return True if not stack else False
        