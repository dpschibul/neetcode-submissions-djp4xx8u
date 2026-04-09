class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #  Input: s = "neetecode", wordDict = ["neet", "neete", "e"]
        memo = {}
        def dfs(sub):
            if sub in memo:
                return memo[sub]
            if len(sub) == 0:
                return True
            
            for word in wordDict:
                if len(word) <= len(sub) and sub[0:len(word)] == word:
                    if dfs(sub[len(word):]):
                        return True
            memo[sub] = False
            return False

        return dfs(s)
