class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_dict = {}

        for i, n in enumerate(nums):
            if target - n in target_dict:
                return [target_dict[target - n], i]
            target_dict[n] = i
        return [-1, -1]        