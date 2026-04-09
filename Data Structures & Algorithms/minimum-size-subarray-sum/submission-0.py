class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums)+1

        for i, n in enumerate(nums):
            if n == target:
                return 1
            cur = n
            j = i + 1
            while j < len(nums) and cur < target:
                cur += nums[j]
                j += 1
            if cur >= target:
                res = min(res, j-i)



        if res == len(nums)+1:
            return 0 
        return res
        