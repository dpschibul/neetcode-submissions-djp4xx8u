class Solution:
    def specialArray(self, nums: List[int]) -> int:
        cnt = [0] * (len(nums)+1)

        for i in range(1, len(nums) + 1):
            for j in range(len(nums)):
                if nums[j] >= i:
                    cnt[i] += 1


        print(cnt)
        for i in range(1, len(nums)+1):
            if cnt[i] == i:
                return i 

        return -1
        
