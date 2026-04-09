class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        longest=1 if len(nums) > 0 else 0

        for n in nums:
            l=0
            curr=n
            if curr-1 not in nums:
                while curr in nums:
                    l+=1
                    curr+=1
                longest=max(longest, l)
        return longest


        