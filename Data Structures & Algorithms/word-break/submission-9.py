class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(word):
            if word in memo:
                return memo[word]
            if word == "":
                return True
            
            for w in wordDict:
                if len(w) <= len(word):
                    if word[:len(w)] == w:
                        if dfs(word[len(w):]):
                            memo[word] = True
                            return True
            memo[word] = False
            return False
        
        return dfs(s)



        