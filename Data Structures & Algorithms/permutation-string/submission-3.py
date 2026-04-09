class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i, c in enumerate(s2):
            cur = i
            s1_set = list(s1)
            while cur < len(s2) and s2[cur] in s1_set:
                s1_set.remove(s2[cur])
                cur+=1
                if not s1_set:
                    return True
        return False

            
        