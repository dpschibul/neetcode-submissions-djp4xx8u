class Solution:
    def isValid(self, s: str) -> bool:
        open_closed = {"}":"{", "]": "[", ")":"("}
        stack = []

        for c in s:
            if c in open_closed:
                if not stack or open_closed[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        print(stack)
        return len(stack) == 0


        