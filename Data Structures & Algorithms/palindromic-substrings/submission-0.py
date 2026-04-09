class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            l, r = i, i
            while r < len(s) and l >= 0:
                if s[l] != s[r]:
                    break
                count += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            l, r = i, i+1
            while r < len(s) and l >= 0:
                if s[l] != s[r]:
                    break
                count += 1
                l -= 1
                r += 1


        return count 

        