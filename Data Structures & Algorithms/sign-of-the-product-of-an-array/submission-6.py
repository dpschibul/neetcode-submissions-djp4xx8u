class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1 

        for n in nums:
            res *= n
        
        return 1 if res > 0 else 0 if res == 0 else -1
        