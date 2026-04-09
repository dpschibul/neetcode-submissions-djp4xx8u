class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for n in nums:
            if 1 > len(nums)//2 or (n in count and count[n]+1 >= len(nums)//2):
                return n
            count[n] = 0 if n not in count else count[n]+1
        
        return 0 