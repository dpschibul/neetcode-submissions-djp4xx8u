class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)
        res = right


        def canSplit(largest):
            subarray = 0
            cur = 0

            for n in nums:
                if cur + n > largest:
                    subarray += 1 
                    cur = n
                else:
                    cur += n
            
            if subarray + 1 > k:
                return False
            return True
        while left <= right:
            mid = left + (right - left) // 2

            if canSplit(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
                

        return res

