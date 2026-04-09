class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left, right = 0, 0
        total = 0
        while right < len(s):
            if s[right] in last_seen and last_seen[s[right]] >= left:
                left = last_seen[s[right]]+1
            total = max(total, right-left+1)
            last_seen[s[right]] = right
            right+=1
        return total

            

        #  "zxyzxyz"
        # {0:z, 1: x}
        # left = 0, right=1
        # c = x
        # check if c is in map
        # if c-index >= left and c in map 
        
        