class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k range = 1...max(piles)
        #          [1,4,3,2]
        #//k (k=2)  1, 2, 2, 1 <= 4h return l
        #//k (k=3)  1, 2, 1, 1 <= 4h return l 
        l, r = 1, max(piles)
        res = r
        while l <= r: # 1, 4
            k = l + (r-l) // 2 # k = 2

            s = 0
            for p in piles:
                pos = math.ceil(p / k)
                s += pos # [1, 2, 2, 1]
            
            if s <= h:
                res = min(k, res)
                r = k - 1
            else:
                l = k + 1
        return res