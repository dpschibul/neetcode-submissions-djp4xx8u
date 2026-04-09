class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        map = defaultdict(int)
        map[0] = 1
        sum = 0

        for n in nums:
            sum += n


            res += map[sum - k]
            map[sum] += 1
        return res

        