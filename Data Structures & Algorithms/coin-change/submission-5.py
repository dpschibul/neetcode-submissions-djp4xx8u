class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(cur):
            if cur in dp:
                return dp[cur]
            if cur == 0:
                return 0
            
            dp[cur] = float('inf')
            for coin in coins:
                if cur - coin >= 0:
                    dp[cur] = min(1 + dfs(cur - coin), dp[cur])
            return dp[cur]

        minCoins = dfs(amount)
        return -1 if minCoins == float('inf') else minCoins

        