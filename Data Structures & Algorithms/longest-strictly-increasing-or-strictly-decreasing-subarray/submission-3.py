class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 1
        incr_count = 1
        decr_count = 1

        for i in range(len(nums)-1):
            n1, n2 = nums[i], nums[i + 1]

            if n1 < n2:
                incr_count += 1
                decr_count = 1
            elif n1 > n2:
                decr_count += 1
                incr_count = 1
            else:
                decr_count = 1
                incr_count = 1
            
            longest = max(longest, incr_count, decr_count)
        
        return longest
        