class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for n in range(amount + 1):
            for coin in coins:
                total = n + coin
                if total <= amount:
                    dp[total] = min(dp[total], 1 + dp[n])
        
        return dp[amount] if dp[amount] != float('inf') else -1
        # memo = {}
        
        # def dfs(n):
        #     if n in memo:
        #         return memo[n]
        #     if n == amount:
        #         return 0
            
        #     memo[n] = float('inf')
        #     for coin in coins:
        #         total = n + coin
        #         if total <= amount:
        #             memo[n] = min(memo[n], 1 + dfs(total))
        #     return memo
            
        # res = dfs(0)
        # return res if res != float('inf') else -1
                