class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        def _rob(nums):
            rob1, rob2 = nums[0], max(nums[0], nums[1])

            for i in range(2, len(nums)):
                temp = max(rob2, rob1 + nums[i])
                rob1 = rob2
                rob2 = temp
            
            return rob2
        
        return max(_rob(nums[1:]), _rob(nums[0:-1]))
        