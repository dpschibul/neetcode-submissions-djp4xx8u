class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        val_set = set(nums)
        res = 0

        for n in nums:
            if n - 1 not in val_set:
                cur = n
                while cur in val_set:
                    cur += 1
                res = max(res, cur - n)
        
        return res
        