class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res=[]

        def dfs(i, cur_nums, total):
            if total == target:
                res.append(cur_nums.copy())
                return
            if total > target or i >= len(candidates):
                return

            cur_nums.append(candidates[i])
            dfs(i+1, cur_nums, total + candidates[i])
            cur_nums.pop()


            i+=1            
            while len(candidates) > i and candidates[i] == candidates[i-1]:
                i +=1

            dfs(i, cur_nums, total)

        dfs(0, [], 0)

        return res
        