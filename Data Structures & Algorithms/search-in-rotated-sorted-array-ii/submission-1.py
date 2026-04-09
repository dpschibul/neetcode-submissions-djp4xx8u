class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        pivot = len(nums)-1

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                pivot = i-1
                break
        
        left, right = 0, pivot
        if target < nums[0]:
            left, right = pivot+1, len(nums)-1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True
            if nums[mid] < target:
                left=mid+1
            else:
                right=mid-1
        return False

        