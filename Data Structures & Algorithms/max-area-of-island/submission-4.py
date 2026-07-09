class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [[1,0], [-1,0], [0,1], [0, -1]]

        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                return 0
            
            count = 0
            grid[r][c] = 0
            for dir in directions:
                count += dfs(r + dir[0], c + dir[1])
            return 1 + count
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        return res