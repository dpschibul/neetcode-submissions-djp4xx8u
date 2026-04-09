class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        avail = set(nums)
        
        def backtrack():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for n in nums:
                if n in avail:
                    avail.remove(n)
                    perm.append(n)
                    
                    backtrack()

                    avail.add(n)
                    perm.pop()
                

        backtrack()
        return res


        