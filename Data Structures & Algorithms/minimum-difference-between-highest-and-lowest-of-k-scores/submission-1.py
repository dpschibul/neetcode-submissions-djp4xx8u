class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minimized = nums[-1] - nums[0]

        for i in range(k-1, len(nums)):
            r = nums[i-k+1: i+1]
            minimized = min(minimized, r[-1] - r[0])
        return minimized
        