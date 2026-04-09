class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            tmp = curMax * n
            curMax = max(curMin * n, curMax * n, n)
            curMin = min(curMin * n, tmp, n)
            res = max(res, curMax)

        return res
            
        