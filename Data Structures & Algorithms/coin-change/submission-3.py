class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for i in range(amount):
            cur = i+1
            for coin in coins:
                if cur - coin >= 0:
                    dp[cur] = min(dp[cur], 1 + dp[cur - coin])
                

        return dp[amount] if dp[amount] != amount + 1 else -1
        