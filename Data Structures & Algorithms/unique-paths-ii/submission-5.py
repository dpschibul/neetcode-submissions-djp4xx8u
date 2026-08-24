class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        if not obstacleGrid or obstacleGrid[0][0] == 1 or obstacleGrid[ROWS-1][COLS-1] == 1:
            return 0
        
        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    continue
                if r == ROWS - 1 and c == COLS -1:
                    obstacleGrid[r][c] = -1
                    continue
                if r != ROWS-1 and obstacleGrid[r + 1][c] != 1:
                    obstacleGrid[r][c] += obstacleGrid[r + 1][c]
                if c != COLS-1 and obstacleGrid[r][c + 1] != 1:
                    obstacleGrid[r][c] += obstacleGrid[r][c + 1]
        return abs(obstacleGrid[0][0])



        # memo = { (ROWS - 1, COLS - 1): 1}


        # def dfs(r, c):
        #     if r >= ROWS or c >= COLS or obstacleGrid[r][c] == 1:
        #         return 0
        #     if (r,c) in memo:
        #         return memo[(r, c)]

            
        #     memo[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
        #     return memo[(r, c)]
        
        # return dfs(0, 0)

        # return immidiatly if (0, 0) == 1 or (r-1, c-1) == 1 
        # [[-3,-2,-1],
        # [-1,-1,-1],
        # [0,1,-1]]