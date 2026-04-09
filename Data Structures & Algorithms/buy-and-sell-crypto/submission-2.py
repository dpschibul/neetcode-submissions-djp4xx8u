class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0

        l, r = 0, 1

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
                continue
            res = max(res, prices[r] - prices[l])

            r += 1
        return res 

            # [10,8,7,5,2]
            # res = 0
            # l = 4, r = 5, p[l] = 5, p[r] = 2
            # 


        