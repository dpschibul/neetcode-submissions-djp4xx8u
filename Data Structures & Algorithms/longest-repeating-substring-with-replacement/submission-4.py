class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        l, r = 0, 0
        res = 0

        while r < len(s):
            count[ord(s[r]) - ord('A')] += 1
            
            cur_window = r - l + 1 - max(count)

            if cur_window <= k:
                res = max(res, r-l + 1)
            else:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
            r += 1
        return res



        