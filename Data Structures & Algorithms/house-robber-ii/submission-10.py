class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]


        def hr1(nums: List[int]):
            memo = [0] * (len(nums) + 2)

            for i in range(len(nums)-1, -1, -1):
                memo[i] = max(memo[i + 1], nums[i] + memo[i + 2])
            
            return memo[0]
    
        return max(hr1(nums[:-1]), hr1(nums[1:]))
        