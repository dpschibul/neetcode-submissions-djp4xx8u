class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[0] * COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    top = 0 if r == 0 else dp[r-1][c]
                    left = 0 if c == 0 else dp[r][c-1]
                    dp[r][c] = grid[r][c] + top + left
                    continue
                dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1])
        return dp[ROWS-1][COLS-1]
        



# grid = [
#     [1,2,0],
#     [5,4,2],
#     [1,1,3]
# ]

# [1, 3, 3]
# [6, 7, 5]
# [7, 8, 8]