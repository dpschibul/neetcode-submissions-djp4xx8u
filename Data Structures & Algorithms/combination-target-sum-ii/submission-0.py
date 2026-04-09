class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res=[]

        def dfs(i, cur_nums):
            if sum(cur_nums) == target:
                res.append(cur_nums.copy())
                return
            if sum(cur_nums) > target or i >= len(candidates):
                return

            cur_nums.append(candidates[i])
            i += 1
            dfs(i, cur_nums)

            cur_nums.pop()
            
            while len(candidates) > i and candidates[i] == candidates[i-1]:
                i +=1

            dfs(i, cur_nums)

        dfs(0, [])

        return res
        