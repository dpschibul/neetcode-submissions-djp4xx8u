def is_palindrome(s: str) -> bool: 
    if not s:
        return False
    left, right = 0, len(s)-1   

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1                 
        right -= 1

    return True

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []


        def backtrack(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if is_palindrome(s[i:j+1]):
                    part.append(s[i:j+1])
                    backtrack(j + 1)
                    part.pop()
            

        backtrack(0)

        return res

            

    

        