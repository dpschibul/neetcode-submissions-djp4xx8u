class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if n > 0:
                break
            
            if i > 0 and n == nums[i-1]:
                continue
            
            left, right = i+1, len(nums)-1
            while left < right:
                total = n + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
                    while nums[left] == nums[left-1] and left < right:
                        left+=1
                elif total < 0:
                    left+=1
                else:
                    right-=1
        return res

        