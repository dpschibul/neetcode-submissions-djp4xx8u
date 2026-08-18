class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        min_heap = []
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i], i))
        
        while k:
            num, idx = heapq.heappop(min_heap)
            heapq.heappush(min_heap, (num * multiplier, idx))
            k -= 1
        
        res = [0] * len(nums)

        for num, idx in min_heap:
            res[idx] = num
        
        return res


        