class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set(nums)

        posInteger = 1
        while posInteger in num_set:
            posInteger += 1
        
        return posInteger
        