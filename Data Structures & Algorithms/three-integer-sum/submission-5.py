class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        a = 0

        while a < len(nums)-2:
            b, c = a+1, len(nums)-1
            while b < c:
                cur_sum = nums[a] + nums[b] + nums[c]
                if cur_sum == 0:
                    res.append([nums[a], nums[b], nums[c]])
                    b+=1
                    c-=1
                    while b < c and nums[b] == nums[b-1]:
                        b+=1
                if cur_sum < 0:
                    b+=1
                if cur_sum > 0:
                    c-=1

            a += 1
            while a < len(nums)-2 and nums[a] == nums[a-1]:
                a += 1

        return res

        