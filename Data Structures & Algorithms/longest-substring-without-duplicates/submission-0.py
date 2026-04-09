class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currChars = []
        l, r = 0, 0
        res = 0

        while r < len(s):
            while s[r] in currChars:
                currChars = currChars[1::] 
                l+=1
            currChars.append(s[r])
            r += 1
            res = max(res, len(currChars))
        return res

        