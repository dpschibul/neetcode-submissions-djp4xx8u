class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        present = set(nums)
        for i in range(len(nums) + 1):
            if i not in present:
                return i
        return -1
        