class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        cur = 0
        
        for c in t:
            if c == s[cur]:
                cur+=1
            if cur == len(s):
                return True
            
        return False

        