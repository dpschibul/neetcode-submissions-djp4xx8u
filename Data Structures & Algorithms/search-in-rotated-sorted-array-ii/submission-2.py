class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums)-1
        # [3,4,4,5,6,1,2,2]
        #  mid = 3

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True
            if nums[mid] > nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[left]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            else:
                left += 1

        return False



        