class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumpsleft = 0

        for num in nums[:-1]: 
            if num == 0 and jumpsleft == 0:
                return False
                
            jumpsleft = max(jumpsleft, num)
            jumpsleft -= 1

        return True