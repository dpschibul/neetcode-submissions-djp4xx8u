class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "]":
                cur = ""
                while stack:
                    val = stack.pop()
                    if val == "[":
                        num = ""
                        while stack and stack[-1].isdigit():
                            num+= stack.pop()
                        stack.append(int(num[::-1]) * cur)
                        break
                    else:
                        cur = val + cur
            else:
                stack.append(c)
        return "".join(stack)