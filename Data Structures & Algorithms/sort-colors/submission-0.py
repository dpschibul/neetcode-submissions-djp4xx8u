class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def is_sorted(arr):
            for i in range(1, len(nums)):
                if nums[i - 1] > nums[i]:
                    return False
            return True
        
        while not is_sorted(nums):
            for i in range(1, len(nums)):
                if nums[i - 1] > nums[i]:
                    nums[i - 1], nums[i] = nums[i], nums[i - 1]
        

        


        