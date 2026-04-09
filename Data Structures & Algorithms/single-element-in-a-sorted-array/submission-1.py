class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if len(nums) == 1:
            return nums[0]

        if nums[l] != nums[l + 1]:
            return nums[l]
        
        if nums[r] != nums[r - 1]:
            return nums[r]

        l, r = l + 1, r - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            left_pos = mid - 1 if nums[mid] == nums[mid+1] else mid
            
            if left_pos % 2 != 0:
                l = mid + 1
            else:
                r = mid - 1 
        return -1
            
        