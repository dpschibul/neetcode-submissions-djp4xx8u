class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        count = [0] * 26 # ord('A') - ord('A') == 0
        length = 0
        res = 0

        while r < len(s):
            count[ord(s[r]) - ord('A')] += 1
            length += 1
            while length - max(count) > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
                length-=1
            
            res = max(length, res)
            r += 1
        return res