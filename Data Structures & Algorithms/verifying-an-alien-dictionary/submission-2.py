class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        orderInd = { c : i for i, c in enumerate(order)}

        for i in range(1, len(words)):
            word1 = words[i-1]
            word2 = words[i]
            for j in range(len(word1)):
                if j == len(word2):
                    return False
                if word1[j] != word2[j]:
                    if orderInd[word2[j]] < orderInd[word1[j]]:
                        return False
                    break
        return True

        