class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def dfs(total):
            if total in memo:
                return memo[total]
            if total > target:
                return 0
            if total == target:
                return 1
            
            res = 0
            for n in nums:
                res += dfs(total + n)
            memo[total] = res
            return res
        return dfs(0)
            


