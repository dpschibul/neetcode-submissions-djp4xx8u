class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def expanding_palindrome(l, r):
            nonlocal count 
            while r < len(s) and l >= 0:
                if s[l] != s[r]:
                    break
                count += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            expanding_palindrome(i, i)
            expanding_palindrome(i, i+1)


        return count 

        