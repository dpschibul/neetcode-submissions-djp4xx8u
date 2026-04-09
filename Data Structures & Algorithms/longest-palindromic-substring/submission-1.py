class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        longest = ""
        
        for i in range(len(s)):
            # Check odd-length palindromes (single center)
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:  # ✅ l >= 0, not l > 0
                if r - l + 1 > len(longest):
                    longest = s[l:r+1]  # ✅ r+1 to include r
                l -= 1
                r += 1
            
            # Check even-length palindromes (two-character center)
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(longest):
                    longest = s[l:r+1]
                l -= 1
                r += 1
        
        return longest