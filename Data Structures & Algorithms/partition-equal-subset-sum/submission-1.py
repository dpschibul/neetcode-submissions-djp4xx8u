class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums) 
        if total % 2 != 0:
            return False
        target = total // 2
        sum_set = set()
        sum_set.add(0)

        for i in range(len(nums)-1, -1, -1):
            for s in sum_set.copy():
                sum_set.add(s + nums[i])
            if target in sum_set:
                return True
        return False


        

        return True