class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in diff:
                return [diff[difference], i]
            diff[n] = i

        return [-1, -1]
