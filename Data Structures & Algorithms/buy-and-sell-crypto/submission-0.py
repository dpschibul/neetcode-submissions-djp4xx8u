class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = int(max(prices))
        res = 0

        for p in prices:
            res = max(res, p - m)
            m = min(p, m)
        return res
        