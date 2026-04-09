class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSequence = 0 
        for n in nums:
            sequence = 0
            if n-1 not in numSet:
                curr = n
                while curr in numSet:
                    sequence += 1
                    curr+=1
            longestSequence = max(sequence, longestSequence)
        return longestSequence
                
