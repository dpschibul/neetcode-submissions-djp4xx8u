class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        cur = deque()
        res = 0

        for r in range(len(s)):
            while s[r] in cur:
                l += 1
                cur.popleft()
            cur.append(s[r])
            res = max(res, len(cur))
        return res

        