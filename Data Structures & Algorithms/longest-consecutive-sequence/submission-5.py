class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestSequence = 0 
        for n in nums:
            sequence = 0
            if n-1 not in nums:
                curr = n
                while curr in nums:
                    sequence += 1
                    curr+=1
            longestSequence = max(sequence, longestSequence)
        return longestSequence
                
