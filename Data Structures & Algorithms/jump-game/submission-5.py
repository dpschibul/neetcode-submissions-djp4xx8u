class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(nums)-1:
                memo[i] = True
                return True
            
            max_jump = nums[i]

            for jump in range(1, max_jump + 1):
                if dfs(jump + i):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        dfs(0)
        
        return memo.get(len(nums) - 1, False)
        