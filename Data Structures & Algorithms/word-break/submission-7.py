class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #  Input: s = "neetecode", wordDict = ["neet", "neete", "e"]

        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if len(s) >= len(word) + i and word == s[i:i+len(word)]:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
        return dp[0]



        
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
