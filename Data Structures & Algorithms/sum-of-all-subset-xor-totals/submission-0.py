class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def backtrack(i, sub):
            nonlocal res
            xxor = 0
            for n in sub:
                xxor ^= n
            res += xxor

            for j in range(i, len(nums)):
                sub.append(nums[j])
                backtrack(j + 1, sub)
                sub.pop()
        
        backtrack(0, [])
        return res

        