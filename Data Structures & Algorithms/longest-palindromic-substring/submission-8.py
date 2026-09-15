class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return 0
        longest = ""

        def isPalindrome(p):
            return p == p[::-1]

        for i in range(len(s)):
            l, r = i, i

            while isPalindrome(s[l:r+1]) and l >= 0 and r < len(s):
                if r + 1 - l > len(longest):
                    longest = s[l:r+1]
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while isPalindrome(s[l:r+1]) and l >= 0 and r < len(s):
                if r + 1 - l > len(longest):
                    longest = s[l:r+1]
                l -= 1
                r += 1
            
        return longest


        