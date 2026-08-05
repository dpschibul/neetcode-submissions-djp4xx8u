class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)

            print(stone1, stone2)

            if stone1 == stone2:
                continue
            
            heapq.heappush(heap, stone1 - stone2)
        
        return abs(heap[-1]) if heap else 0