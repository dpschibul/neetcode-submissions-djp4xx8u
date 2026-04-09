class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sortedSet = sorted(set(nums))
        longest = 1
        currSequenceCount = 1
        lastValue = nums[0]

        for n in sortedSet:
            if n == lastValue+1:
                currentSequenceCount+=1
            else:
                currentSequenceCount = 1
            longest = max(longest, currentSequenceCount)
            lastValue=n

        return longest