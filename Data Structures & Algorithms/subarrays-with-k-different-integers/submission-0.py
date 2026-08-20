class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        far, near = 0, 0

        window = defaultdict(int)
        res = 0

        for r in range(len(nums)):
            window[nums[r]] += 1

            while len(window) > k:
                window[nums[near]] -= 1
                if window[nums[near]] == 0:
                    window.pop(nums[near])
                near += 1
                far = near
            

            while window[nums[near]] > 1:
                window[nums[near]] -= 1
                near += 1

            if len(window) == k:
                res += near - far + 1
            

        return res
            
        
        