class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = []

        for r in range(len(triangle)):
            dp.append([])
            for c in range(len(triangle[r])):
                dp[r].append(float('inf'))

        for r in range(len(triangle)-1, -1, -1):
            for c in range(len(triangle[r])-1, -1, -1):
                if r == len(triangle)-1:
                    dp[r][c] = triangle[r][c]
                    continue
                dp[r][c] = triangle[r][c] + min(dp[r + 1][c], dp[r + 1][c + 1])
        
        return dp[0][0]

        memo = {}

        # def dfs(i, j):
        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     if i >= len(triangle) or j >= len(triangle[i]):
        #         return 0
            
        #     memo[(i, j)] = min(triangle[i][j] + dfs(i + 1, j), triangle[i][j] + dfs(i + 1, j + 1))
        #     return memo[(i, j)]

        # return dfs(0, 0)
        