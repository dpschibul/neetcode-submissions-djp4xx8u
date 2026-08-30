class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0

        for i in range(len(nums)):
            cur = 0
            for j in range(i, len(nums)):
                cur += nums[j]
                if cur % k == 0:
                    res += 1

        return res

        