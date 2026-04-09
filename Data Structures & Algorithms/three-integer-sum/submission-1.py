class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        out = []

        for i, n in enumerate(nums):
            if i > 0 and nums[i - 1] == n:
                continue
            l, r = i + 1, len(nums)-1
            while l < r:
                curr = nums[l] + nums[r]
                if n + curr == 0:
                    out.append([n, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                if n + curr < 0:
                    l+=1
                if n + curr > 0:
                    r-=1
        return out



        