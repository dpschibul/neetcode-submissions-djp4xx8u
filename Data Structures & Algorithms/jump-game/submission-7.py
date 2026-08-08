class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {len(nums) - 1: True}
        
        for i in range(len(nums)-1, -1, -1):
            for j in range(1, nums[i] + 1):
                if memo.get(i + j, False):
                    memo[i] = True
                    break
            if i not in memo:
                memo[i] = False
        return memo[0]



        