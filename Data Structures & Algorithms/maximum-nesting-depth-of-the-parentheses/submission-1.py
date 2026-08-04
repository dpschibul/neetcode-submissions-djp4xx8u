class Solution:
    def maxDepth(self, s: str) -> int:

        stack = []
        depth = 0

        for c in s:
            if c == '(':
                stack.append(c)
            if c == ')':
                stack.pop()
            
            depth = max(depth, len(stack))
        return depth

