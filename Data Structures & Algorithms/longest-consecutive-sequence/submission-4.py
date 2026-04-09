class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            streak, curr = 0, n
            while curr in numSet:
                streak +=1
                curr +=1
            longest = max(longest, streak)

        return longest