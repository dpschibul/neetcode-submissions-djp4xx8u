class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter = Counter(s)
        tcounter = Counter(t)

        for c in t:
            if c not in counter:
                return c
            if counter[c] < tcounter[c]:
                return c
        return ""
        