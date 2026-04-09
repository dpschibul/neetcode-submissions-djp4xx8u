class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [1] * len(nums), [1] * len(nums)
        res = []
        for i in range(1, len(nums)):
            j = len(nums) - 1 - i
            prefix[i] = prefix[i-1] * nums[i-1]
            postfix[j] = postfix[j+1] * nums[j+1]
        
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i])

        return res
        # [1,2,4,6]
        # [1, 1, 2, 8]
        # [48, 24, 6, 1]

        # [-1,0,1,2,3]
        # [0, 6, 6, 3, 1]
        # [1, -1, 0, 0, 0]
        
        


        