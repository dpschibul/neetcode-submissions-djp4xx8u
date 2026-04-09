class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        p1 = 0
        p2 = 0

        while p1 < len(word1) and p2 < len(word2):
            if len(res) % 2 == 0:
                res += word1[p1]
                p1 += 1
            else:
                res += word2[p2]
                p2 +=1
        
        res += word1[p1:]
        res += word2[p2:]

        return res


        