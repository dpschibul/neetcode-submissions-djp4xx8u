class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [False] * len(nums)
        memo[-1] = True
        
        for i in range(len(nums)-1, -1, -1):
            max_jump = min(nums[i] + 1, len(nums) - i)
            print(max_jump)
            for j in range(1, max_jump):
                if memo[i + j]:
                    memo[i] = True
                    break

        return memo[0]



        