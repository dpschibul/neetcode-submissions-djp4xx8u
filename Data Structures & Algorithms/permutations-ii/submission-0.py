class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        count = Counter(nums)

        def backtrack():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for key, val in count.items():
                if val >= 1:
                    perm.append(key)
                    count[key] -= 1

                    backtrack()

                    count[key] += 1
                    perm.pop()
        backtrack()
        return res
                




        