class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def house_robber_one(nums: List[int]) -> int:
            rob1, rob2 = 0, 0

            for n in nums:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2

        return max(house_robber_one(nums[1:]), house_robber_one(nums[0:len(nums)-1]))

            
        