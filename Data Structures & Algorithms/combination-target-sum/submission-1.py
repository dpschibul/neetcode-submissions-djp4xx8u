class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        
        def backtrack(i, curSum):
            if curSum == target:
                res.append(comb.copy())

            for j in range(i, len(nums)):
                if nums[j] + curSum <= target:
                    comb.append(nums[j])
                    backtrack(j, curSum + nums[j])
                    comb.pop()
        backtrack(0, 0)

        return res