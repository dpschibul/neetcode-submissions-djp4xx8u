class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1, stone2 = abs(heapq.heappop(stones)), abs(heapq.heappop(stones))
            leftover_stone = stone1 - stone2
            if leftover_stone > 0:
                heapq.heappush(stones, -leftover_stone)
            
        return abs(stones[0]) if stones else 0