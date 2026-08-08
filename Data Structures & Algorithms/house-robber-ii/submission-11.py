class Solution:
    def rob(self, nums: List[int]) -> int:


        def hr1(nums: List[int]):
            rob1, rob2 = 0, 0

            for i in range(len(nums)-1, -1, -1):
                newRob = max(nums[i] + rob1, rob2)
                rob1 = rob2
                rob2 = newRob
            
            return rob2
    
        return max(hr1(nums[:-1]), hr1(nums[1:]), nums[0])
        