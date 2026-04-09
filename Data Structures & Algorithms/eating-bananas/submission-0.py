class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        minEatSpeed = r
        while l <= r:
            mid = (r - l)//2+l
            if self.canEatInHours(piles, h, mid):
                minEatSpeed = mid
                r = mid-1
            else:
                l = mid+1
        return minEatSpeed

        
    def canEatInHours(self, piles: List[int], h: int, k: int) -> bool:
        hoursTaken = 0
        for p in piles:
            hoursTaken += max(0, math.ceil(p / k))
        if hoursTaken <= h:
            return True
        return False



            


        