class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        res = right

        def canShip(capacity):
            ships = 1
            cur = 0

            for w in weights:
                if cur + w <= capacity:
                    cur += w
                else:
                    ships+=1
                    cur = w
            return ships <= days

        while left <= right:
            cap = left + (right - left) // 2
            if canShip(cap):
                res = cap
                right = cap-1
            else:
                left = cap+1

        return res


        