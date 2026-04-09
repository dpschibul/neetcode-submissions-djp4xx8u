class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for n in nums:
            count[n] = 0 if n not in count else count[n]+1
        
        for key in count:
            if count[key] >= len(nums)//2:
                return key
        
        return -1
        