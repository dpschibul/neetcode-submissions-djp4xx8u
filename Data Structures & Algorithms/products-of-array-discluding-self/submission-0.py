class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        prefix = 1
        for i, n in enumerate(nums):
            res[i] = prefix
            prefix = prefix * n

        postfix = 1
        for i, n in enumerate(reversed(nums)):
            index = len(nums) - 1 - i
            res[index] = res[index] * postfix
            postfix = postfix * n

        return res