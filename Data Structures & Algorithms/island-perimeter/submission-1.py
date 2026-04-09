class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        res = [0]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(r, c):
            if (r, c) in visit:
                return
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                res[0] += 1
                return 

            visit.add((r,c))

            for direction in directions:
                dfs(r+direction[0], c+direction[1])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return res[0]
        
        return res[0]

        