class Solution:
    def arraySign(self, nums: List[int]) -> int:
        count_neg = 0

        for n in nums:
            if n < 0:
                count_neg +=1
            if n == 0:
                return 0 

            
        

        return -1 if count_neg % 2 == 1 else 1
        