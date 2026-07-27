class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenAt = {}

        for i, n in enumerate(nums):
            if target - n in seenAt:
                return [seenAt[target - n], i]
            seenAt[n] = i
        return [-1, -1]
        