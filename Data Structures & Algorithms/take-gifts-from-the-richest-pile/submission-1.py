import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        pq = []

        for gift in gifts:
            heapq.heappush(pq, -gift)


        
        for i in range(k):
            gift = -heapq.heappop(pq)

            new_val = int(math.sqrt(gift))

            heapq.heappush(pq, -new_val)


        return sum(abs(v) for v in pq)
        