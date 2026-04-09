class Solution:
    def isHappy(self, n: int) -> bool:
        s = str(n)

        nums = set()

        while 1 not in nums:
            sum = 0
            for c in s:
                sum += int(c)**2
            if sum in nums:
                return False
            
            nums.add(sum)
            s=str(sum)
            
        print(nums)
        return True
        