class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(closed, opened, cur):
            if closed == 0 and opened == 0:
                res.append("".join(cur))
                return
            
            if opened == 0 or opened < closed:

                dfs(closed-1, opened, cur + [')'])
            if opened > 0:
                dfs(closed, opened-1, cur + ['('])
        dfs(n, n, [])
        return res
            


        