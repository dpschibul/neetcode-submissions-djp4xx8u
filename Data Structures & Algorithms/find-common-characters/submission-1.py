class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        word1_count = Counter(words[0])

        for i in range(1, len(words)):
            wordi_count = Counter(words[i])

            for c in word1_count:
                word1_count[c] = min(wordi_count.get(c, 0), word1_count[c])
        
        res = []

        for c, count in word1_count.items():
            for i in range(count):

                res.append(c)
        return res
            

                    

        