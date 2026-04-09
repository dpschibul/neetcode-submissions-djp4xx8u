class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            mid = left + (right - left) // 2

            time_to_eat = 0
            for pile in piles:
                time_to_eat += math.ceil(pile / mid)
            
            if time_to_eat <= h:
                right = mid-1
                res = mid
            else:
                left = mid+1
        
        return res