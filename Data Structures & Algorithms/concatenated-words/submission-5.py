class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        memo = {}

        def canBuild(w):
            if w in memo:
                return memo[w]
            memo[w] = False  # avoid infinite recursion on self-match, placeholder
            for i in range(1, len(w)):
                prefix, suffix = w[:i], w[i:]
                if prefix in word_set and (suffix in word_set or canBuild(suffix)):
                    memo[w] = True
                    return True
            return False

        return [w for w in words if canBuild(w)]